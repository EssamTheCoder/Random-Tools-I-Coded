from random import randint

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
        return f'{round(average)}\n'
    
    elif will_round == False:
        return f'{average}\n'
