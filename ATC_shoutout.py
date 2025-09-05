import tools as t
from tools import load_json as getdata
import debuglogger as log

def make_one(text: str):
    splitted = text.split(" ")
    valid_words = [
                "turn left right heading degrees dgr",
                "climb descend and maintain ft",
                "direct to",
                "increase reduce speed to knots"
                "clear for takeoff",
                "go around",
                "extend", "own discretion | base | runway | upwind | crosswind | downwind | final"
    ]
    final_atc = []
    if getdata("user_data.json")["include_callsign"]:
        try:
            final_atc.append(getdata("airlines.json")[splitted[0]]+splitted[1])
            splitted.pop(0)
            splitted.pop(0)
        except:
            t.misc_data.error=True
            return None
    log.write("Entering for-loop")
    for word in splitted:
        if splitted == []:
            break

        for sentence in valid_words:
            if word in sentence.split():
                final_atc.append(word)
            else:
                try: 
                    temp = int(word)
                    final_atc.append(word)
                except:
                    t.misc_data.error=True
                    break

    return final_atc


#def transform():
