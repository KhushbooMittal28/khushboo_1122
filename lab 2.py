L = int(input())
W = int(input())
print("area of given plot is",L*W)

A = int(input())
B = int(input())
print("area of given plot is",A*B*0.3048*0.3048)

x = int(input())
y = int(input())
if x<0 or y<0:
    print('invalid input')
elif (y%x)==0:
    print('y =',y,'is divisible by x =',x,'.')
elif (y%x)!=0:
    print('y =',y,'is not divisible by x =',x,".")



x = int(input('enter an integer: '))
if x%2==0:
    print('integer is even.')
elif x%2!=0:
    print('integer is odd.')


r = int(input('enter the radius of circle: '))
pi = 3.14
a = pi*r**2
if r>=1 and r<=100:
    print('Area of circle is ',a,'sq units.')
else:
    print('enter radius between 1 and 100.')



c = float(input('enter temperature in celsius :'))
f = c*(9/5) +32
k = c+273
print(c,'celsius = ',f,'fahrenheit and ',k,'kelvin.')



for c in range(-273,1000):    # range is in celsius from abosulte zero to 1000 C.
    f = c*(1.8) +32
    if c==f:
        print(c)    



x = int(input('enter the year you wish to check: '))
l = x % 400
if l==0:
    print(x,'is a leap year.')
else:
    print(x,'is not a leap year.')



r = 7.1 # bank calculates interest on RD accounts at 7.1% p.a.
p = float(input('enter the principle amount in rupees: '))
t = float(input('enter the duration of RD in years: '))
n= t*12
if p<500 or t<0.5:
    print('invalid input.')
else:
    a = p*(1+r/100)*n*t
print('amount is Rs ',a)
print('monthly return is ',a/12)



x = int(input('enter the no. of sec :'))
if x in range(1,86400):
    h= x//3600
    m = x//60 - h*60


    s = x- h*3600- m*60
    print(x,'sec =',h,'hours',m,'min','and',s,'sec.')
else:
    print('enter sec in between 1 and 86400.')