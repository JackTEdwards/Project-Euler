def sumMul3and5(n):
    result = 0 

    for i in range(0, n):
        if i%3 == 0 or i%5 ==0:
            result +=i

    return result

if __name__ == '__main__':
    print(sumMul3and5(1000))