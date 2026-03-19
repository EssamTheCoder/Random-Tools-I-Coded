#For anything that you can't test in the ipynb
print("Uno Flip Deck Generator");
print("Version A2.0\n");
from secrets import choice
from numpy import arange as arng
import colorama

def arange(start:int,stop:int):
    return list(arng(start,stop))

def __main__():
    lightCards = ["0","1","2","3","4","5","6","7","8","9","Skip","Reverse","Flip","+2"]
    darkCards = ["0","1","2","3","4","5","6","7","8","9","Skip All","Reverse","Flip","+2"]

    lightWilds = ["Wild","Wild Draw Colour"]
    darkWilds = ["Wild","Wild +4"]

    reds = []
    blues = []
    greens = []
    yellows = []

    purples = []
    magentas = []
    oranges = []
    teals = []

    loopedArray = [i for i in list(range(0,14)) for d in range(2)]
    for l in loopedArray:
        reds.append(f"{lightCards[l]}")
        blues.append(f"{lightCards[l]}")
        greens.append(f"{lightCards[l]}")
        yellows.append(f"{lightCards[l]}")
    
    for d in loopedArray:
        purples.append(f"{darkCards[d]}")
        magentas.append(f"{darkCards[d]}")
        oranges.append(f"{darkCards[d]}")
        teals.append(f"{darkCards[d]}")



    while True:
        cardPair = {
            "light": "",
            "seperator": " -> ",
            "dark": ""
        }

if __name__ == "__main__":
    __main__()