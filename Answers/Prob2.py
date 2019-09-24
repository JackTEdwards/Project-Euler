def sumEvenFibonacci(n):
    curr = 1
    prev = 1
    result = 0

    while curr <= n:
        if curr%2 == 0:
            result += curr
        
        curr, prev = curr + prev, curr
    
    return result

if __name__ == '__main__':
    print(sumEvenFibonacci(4000000))