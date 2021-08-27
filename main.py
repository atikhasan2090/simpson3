
def func(x):
    return 1/(x*x+1)




s = 0
a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))
n = int(input("Enter the number of Sub interval: "))
h = (b-a)/n
for i in range(1,n):
    x = a + (i*h)
    if(i%2==0):
        s = s+2*func(x)
    else:
        s = s+4*func(x)

s = (func(a) + func(b) + s)*h/3
print("Area is : ",s)









