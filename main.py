import MicManager 
import speechConverter as sc
import ATC_shoutout
import tools


import json

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


while (True):
    Spoken_Raw = sc.listen(1)
    if Spoken_Raw != None:
        ATC_CMD = ATC_shoutout.make_one(Spoken_Raw)
        if tools.misc_data.error == True:
            sc.speak("Say again.")
            tools.misc_data.error = False
        else: 
            sc.speak(ATC_CMD)
