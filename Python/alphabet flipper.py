def __main__(inp: str) -> str:
    out = ""
    for i in range(0,len(inp)):
        currentChar = inp[i]
        if currentChar.isalpha() == True:
            if currentChar.islower() == True:
                out += currentChar.capitalize()
            else:
                out += currentChar.lower()
        else:
            out += currentChar

    return out

while True:
    print(__main__(input("What text do you want to reverse capitalisation for? ")))
