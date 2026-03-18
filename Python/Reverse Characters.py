print("String Reverser");
print("V1.0\n");

def fullReverse(text:str):
    text = list(reversed(text))
    temp = ""
    for i in range(0,len(text)):
        temp += text[i]
    return temp

def wordReverse(text:str):
    text = text.split(" ")
    textStr = ""
    temp = []
    for i in range(0,len(text)):
        temp.append(list(reversed(text[i])))
    
    for i in range(0,len(temp)):
        counter = -1
        for j in temp[i]:
            if len(j) == counter: 
                counter += 1
            textStr += j[counter]
        textStr += " "
    
    return textStr



counter = 0
while True:
    counter += 1

    if counter == 1:
        print("---MODES---")
    else:
        print("\n---MODES---")
    print("1. FULL REVERSE - Parses the text as 1 string and reverses it.")
    print("2. WORD REVERSE - Seperates the string into individual words and reverses them individually.")

    mode = ""
    while type(mode) != int:
        try:
            mode = int(input("Pick a mode. "))
        except ValueError:
            mode = int(input("Input them using numbers. "))

    inp = input("\nWhat text do you want to reverse? ")

    if mode == 1:
        print(fullReverse(inp))
    elif mode == 2:
        print(wordReverse(inp))
