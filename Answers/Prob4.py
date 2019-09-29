def isPalindrome(n):
    nArray = list(map(int, str(n)))
    nArrayReversed = list(reversed(nArray))
    
    for i in range (len(nArray)):
        if nArray[i] != nArrayReversed[i]:
            return False 
    
    return True

def findLargestPalindrome(n):
    lowestVal = 10**(n-1)
    highestVal = (10**n)
    returnVal = 0

    for i in range(lowestVal, highestVal):
        for j in range (lowestVal, highestVal):
            val = i*j
            if (isPalindrome(val) and val > returnVal):
                returnVal = val
    
    return returnVal         

if __name__ == '__main__':
    print(findLargestPalindrome(3))