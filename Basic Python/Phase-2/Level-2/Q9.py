"""Print Fibonacci series up to n terms."""

def fibonacciSeries(n):
    a , b =0,1
    if n <= 0:
        print("Enter positive Number")
    elif n == 1:
        print(n)
    else:
        print("fibonacci series:")

        for i in range(n):
            print(b,end= " ")
            a , b = b , a+b


fibonacciSeries(10)