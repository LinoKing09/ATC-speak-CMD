import whisper
import sounddevice as sd
import numpy as np
import queue
import torch
import sys

# Load Whisper model (small = good speed/accuracy balance)
model = whisper.load_model("small")

# Audio queue
q = queue.Queue()

# Audio callback -> add to queue
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

samplerate = 16000
with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, blocksize=int(samplerate*1)):
    print("🎙️ Live transcription (Ctrl+C to stop):\n")

    buffer = np.zeros(0, dtype=np.float32)

    try:
        while True:
            data = q.get()
            audio = np.squeeze(data).astype(np.float32)

            # Append to rolling buffer
            buffer = np.concatenate((buffer, audio))

            # Keep only last 5 seconds of audio
            if len(buffer) > samplerate * 5:
                buffer = buffer[-samplerate * 5 :]

            # Run Whisper on buffer
            result = model.transcribe(buffer, fp16=torch.cuda.is_available(), language="en")

            # Print "live" transcript, overwrite same line
            text = result["text"].strip()
            sys.stdout.write("\r" + text)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\nStopped.")
