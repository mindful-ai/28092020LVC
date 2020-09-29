# fibo.py


# 0 1 1 2 3 5 8 13...

def genfibo(n):
    fibolist = []
    x = 0
    fibolist.append(x)
    y = 1
    fibolist.append(y)
    for i in range(n-2):
        z = x + y
        fibolist.append(z)
        x = y
        y = z
    return fibolist

def checkfibo(n):
    x = 0
    y = 1
    while True:
        z = x + y
        if(n == z):
            return (0, 0)
        elif(z > n):
            return (abs(n-y), abs(n-z))
        x = y
        y = z

# -----------------------------------


if __name__ == '__main__':

    print(genfibo(12))
    print(checkfibo(44))
