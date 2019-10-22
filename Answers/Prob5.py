def smallestDivisible(n):
    i = 0
    result = 0
    highVal = n-1
    lowVal = n//2
    
    while True:
        i += 1
        testNum = n*i
        isDiv = True

        for j in range(highVal, lowVal, -1):
            if(testNum%j !=0):
                isDiv = False 
                break
        
        if(isDiv):
            result = testNum 
            break

    return result 

if __name__ == '__main__':
    print(smallestDivisible(20))