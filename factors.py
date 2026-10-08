def factor (n):
    factor = []
    for i in range (1, n+1):
        if n % i == 0:
            factor.append(i)
    print(factor)
factor(int(input("give a number: ")))