print("Metti dei numeri interi")
a=int(input("num A = "))
b=int(input("num B = "))
c=int(input("num C = "))
def somma(a,b,c):
    result = a+b+c
    return result

print("A+B+C = {} " .format(somma(a,b,c)))