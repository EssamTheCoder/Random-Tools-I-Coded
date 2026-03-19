print("Random Password Generator");
print("V3.0\n");
import secrets as sec
from numpy import arange

#Lists
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

asciiChars = ["!", ""","#", "$", "%", "&", """, "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", 
		    "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]

nonAsciiChars = ['¡','€','£','¢','∞','§','¶','•','ª','º',"“",'‘','…',
                'æ','«','≤','≥','÷','œ','∑','´','®','¥','¨','^','ø','π','å','ß','∂',
                'ƒ','©','˙','∆','˚','¬','≈','ç','√','∫','~','µ','±',
                '–','≠']

space = [" "]

lists = [upper,lower,nums,asciiChars,nonAsciiChars,space]

def passwordTime(length: int,chars:bool,ascii: bool,spaces: bool):
    #Checks & Inital Changes
    removedLists = []
    if chars == False:
        lists.remove(asciiChars)
        removedLists.append(asciiChars)
    if ascii == False:
        lists.remove(nonAsciiChars)
        removedLists.append(nonAsciiChars)
    if spaces == False:
        lists.remove(space)
        removedLists.append(space)
    
    lastChar = 0
    password = ""

    for p in range(0,length):
        listChoice = sec.choice(lists)
        char = sec.choice(listChoice)
    
        while char == lastChar:
            char = sec.choice(listChoice)
        password += char

    if len(removedLists) != 0:
        for i in removedLists:
            lists.append(i)
    
    return password


def boolProcessing(inp: str, default:bool):
    inp = inp.lower()
    if inp == 'y':
        return True
    elif inp == 'n':
        return False
    elif inp == '':
        return default
    else:
        return "invalid"


def lengthProcessing(length: str) -> None:
    value = length.lower()
    if length.isdecimal() == True:
        value = int(length)
    elif length in ["surprise me","random"]:
        value = sec.choice(arange(20,500,step=1))
    elif len(length) == 0:
        value = 20
    else:
        value = "invalid"
    
    specialCharacters = boolProcessing(input("Would you like to use special characters? (Y/n) "),True)
    asciiOnly = False
    if specialCharacters == True:
        asciiOnly = boolProcessing(input("Would you like to include non-ASCII special characters? (Y/n) "),True)

    supportsSpaces =  boolProcessing(input("Would you like spaces in your password? (y/N) "),False)

    try:
        return passwordTime(value,specialCharacters,asciiOnly,supportsSpaces)
    except ValueError:
        lengthProcessing(input("There was an error, retry. How long is the password? "))

    


def __main__() -> None:
    inp = lengthProcessing(input("How long do you want your password? "))
    print(f"{inp}\n")

while True:
    __main__()
