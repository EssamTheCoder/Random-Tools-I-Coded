#For anything that you can't test in the ipynb
print("Uno Flip Deck Generator");
print("Version A2.0");
print("External Libraries: colorama\n")

from secrets import choice
from typing import Collection
from colorama import init, Fore
init()

def main(sep:str) -> None:
    """
    Prints a fully randomised deck of Uno Flip Cards, sperated by a user-selected string. Defaults to "->" if the user presses enter without entering a string

    :sep: The sperator that sperates the light card from the dark one when printing
    :return: None
    """
    sep = "->" if not sep else sep
    #Lists
    lightCards = ["0","1","2","3","4","5","6","7","8","9","Skip","Reverse","Flip","+2"]
    darkCards = ["0","1","2","3","4","5","6","7","8","9","Skip All","Reverse","Flip","+5"]

    lightWilds = ["Wild","Wild +4"]
    darkWilds = ["Wild","Wild Draw Colour"]

    reds = [f"Red {i}" for i in lightCards+lightCards]
    blues = [f"Blue {i}" for i in lightCards+lightCards]
    greens = [f"Green {i}" for i in lightCards+lightCards]
    yellows = [f"Blue {i}" for i in lightCards+lightCards]

    lightLists = [reds, blues, greens, yellows, lightWilds]

    purples = [f"Purple {i}" for i in darkCards+darkCards]
    magentas = [f"Magenta {i}" for i in darkCards+darkCards]
    oranges = [f"Orange {i}" for i in darkCards+darkCards]
    teals = [f"Teal {i}" for i in darkCards+darkCards]

    darkLists = [purples, magentas, oranges, teals, darkWilds]
    
    colours = ()
    for i in range(0,56):
        colours = ( choice(lightLists), choice(darkLists) )
        card = {
            "light": choice(colours[0]),
            "seperator": f" {sep} ",
            "dark": choice(colours[1])
        }

        colours[0].remove(card["light"])
        colours[1].remove(card["dark"])

        for l in lightLists:
            if not l:
                lightLists.remove(l)
        
        for d in darkLists:
            if not d:
                darkLists.remove(d)

        card["light"] = Fore.RED + card["light"] if "Red" in card["light"] else Fore.BLUE + card["light"] if "Blue" in card["light"] else Fore.GREEN + card["light"] if "Green" in card["light"] else Fore.YELLOW + card["light"] if "Yellow" in card["light"] else card["light"]
        card["dark"] = Fore.MAGENTA + card["dark"] if "Purple" in card["dark"] else Fore.LIGHTMAGENTA_EX + card["dark"] if "Magenta" in card["dark"] else Fore.LIGHTRED_EX + card["dark"] if "Orange" in card["dark"] else Fore.LIGHTBLUE_EX + card["dark"] if "Teal" in card["dark"] else card["dark"]

        print(f"{card["light"]}{Fore.RESET + card["seperator"]}{card["dark"]}")

    print(Fore.RESET + "\n \n")


while __name__ == "__main__":
    main(input("Pick a sperator for your card's two sides: "))