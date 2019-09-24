
def getLargestPrimeFactor(n):
    for x in range(2, n+1):
        if(n == x):
            result = x
            break

        if(n%x == 0):
            result = getLargestPrimeFactor(n//x)
            break
    
    return result

if __name__ == '__main__':
    print(getLargestPrimeFactor(600851475143))