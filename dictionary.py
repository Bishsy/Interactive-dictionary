import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return  data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Is this similar to   %s  that you are looking? Enter y if Yes, or n if No  " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[ get_close_matches(w, data.keys())[0]]
        elif yn ==  "n":
            return "The word doesn't exit, please double check it once"
        else :
            return "We did'nt understand your query "
    else:
        return "The word doesn't exit, please double check it twice "

word =input("Enter the word -")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
