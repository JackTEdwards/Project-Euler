def isPalindrome(n):
    nArray = list(map(int, str(n)))
    nArrayReversed = list(reversed(nArray))
    
    for i in range (len(nArray)):
        if nArray[i] != nArrayReversed[i]:
            return False 
    
    return True


if __name__ == '__main__':
    isPalindrome(11)