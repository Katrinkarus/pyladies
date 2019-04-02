nterms = int(input("How many terms?"))
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a postitive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacii sequence upto", nterms, ":")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

def recur_fibo(n):
    """Recursive function to 
    print Fibonacci sequence"""
    if n <= 1:
        return n 
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("How many terms?"))

if nterms <=0: