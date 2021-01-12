def factorial (n):
    if n==0:
        return 1
    else:
        return fctorial(n-1)*n

def printRev(n):
    if n>0:
        printRev(n-1)
        print(n)

def fibonacci(n):
    if n==1 or n==0:
        return n
    if n > 1:
        return (fibonacci(n-1)+fibonacci(n-2))

def main ():
    for x in range (1,10,1):
        r=factorial(num)
        print(f"el fctorial de {num} es {r}")
main()

def main2():
    printRev(3)

main2()

def main3():
    for num in range(11)
    print(fibonacci(num)+ ",", end="")
    print("")
main3()
