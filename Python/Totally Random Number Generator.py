print("Totally Random Number Gnerator");
print("V1.1\n");
from random import randint, choice

def theRandomiser(start: int, end: int, will_round: bool):
    rangeNum = randint(start,end)
    while rangeNum < end - 5:
        rangeNum = randint(start,end) 

    nums = []
    for i in range(0,rangeNum):
        num = 0
        if i % 3 == 0:
            num = randint(start,rangeNum)
            nums.append(num)
        
        elif i % 3 == 1:
            num = randint(rangeNum,end)
            nums.append(num)
        
        else:
            num = randint(start,end)
            nums.append(num)
    
    average = 0
    for n in range(0,rangeNum):
        if n == 0:
            average = nums[n]
        
        else:
            average += nums[n]

    average /= rangeNum

    if will_round == True:
        print(f'{round(average)}\n')
    
    elif will_round == False:
        print(f'{average}\n')

willRound = input("Should the number be an integer (Y/n)? ").lower()


while True:
    #Start_num
    try:
        start_num = int(input("Starting Number: "))
    except ValueError:
        start_num = int(input("Starting Number, integer please: "))

    #End_num
    try:
        end_num = int(input("End Number: "))
    except ValueError:
        end_num = int(input("End Number, integer please: "))


    while willRound not in ['y','n']:
        willRound = input("Should the number be an integer? Answer yes, no, y or n please. ").lower()

    if willRound == 'y':
        theRandomiser(start_num,end_num,True)
    
    else:
        theRandomiser(start_num,end_num,False)
