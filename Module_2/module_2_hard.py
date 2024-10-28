num = int(input("Enter a number 3-20, or 0 to exit: "))
if 2 < num < 21:
    for i in range(1, num//2+1):
        for j in range(i+1, num):
            if num % (i+j) == 0:
                print(i, j, sep='', end='')
    print()
