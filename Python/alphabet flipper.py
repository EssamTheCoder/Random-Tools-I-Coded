print("Alphabet Flipper");
print("Verison V1.1\n");

def __main__() -> None:
    while True:
        inp:str = input("What text do you want to reverse capitalisation for? ")
        out:str = ""

        for i in range(0,len(inp)):
            currentChar = inp[i]
            if currentChar.isalpha() == True:
                if currentChar.islower() == True:
                    out += currentChar.capitalize()
                else:
                    out += currentChar.lower()
            else:
                out += currentChar
        print(out)

if __name__ == "__main__":
    __main__()
