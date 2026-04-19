print("Random Password Generator");
print("V3.0\n");
import secrets as sec


#Lists
upper = [chr(i) for i in range(63,91)]
lower = [chr(i) for i in range(97,123)]
nums = [chr(i) for i in range(48,58)]
space = [" "]

asciiChars = [chr(i) for i in set(range(33,48)) | set(range(58,64)) | set(range(91,97)) | set(range(123,127))]
extendedAscii = [chr(i) for i in set(range(161, 173)) | set(range(174, 256))]

lists = [upper,lower,nums,asciiChars,extendedAscii,space]

def passwordTime(length:int, chars:bool, ascii:bool, spaces:bool):
    #Checks & Inital Changes
    removedLists = []
    if chars == False:
        lists.remove(asciiChars)
        removedLists.append(asciiChars)
    if ascii == False:
        lists.remove(extendedAscii)
        removedLists.append(extendedAscii)
    if spaces == False:
        lists.remove(space)
        removedLists.append(space)
    
    lastChar = "\0"
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
        value = sec.choice(list(range(20,501)))
    elif len(length) == 0:
        value = 20
    else:
        value = "invalid"
    
    specialCharacters = boolProcessing(input("Would you like to use special characters? (Y/n) "),True)
    asciiOnly = False
    if specialCharacters == True:
        asciiOnly = boolProcessing(input("Would you like to include extended ASCII special characters? (Y/n) "),True)

    supportsSpaces =  boolProcessing(input("Would you like spaces in your password? (y/N) "),False)

    try:
        return passwordTime(value,specialCharacters,asciiOnly,supportsSpaces)
    except ValueError:
        lengthProcessing(input("There was an error, retry. How long is the password? "))

    


def main() -> None:
    print(f"{lengthProcessing(input("How long do you want your password? "))}\n")

while __name__ == '__main__':
    main()
