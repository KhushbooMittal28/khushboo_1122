X = int(input('enter 1st no.: '))
Y = int(input('enter 2nd no.: '))
print('Sum of the numbers = ',X+Y)
print('Difference of numbers = ',X-Y)
print('product of numbers = ',X*Y)
print('division of numbers = ',X/Y)


a = float(input('enter 1st no.: '))
b = float(input('enter 2nd no.: '))
c = float(input('enter 3rd no.: '))
d = float(input('enter 4th no.: '))
avg = (a+b+c+d)/4
print('Average of numbers = ',avg)


P = float(input('Enter the Principle Amount in Rupees: '))
R = float(input('Enter the Rate of Interest: '))
T = float(input('Enter Time Period in Years: '))
SI = (P*R*T)/100
print('Simple Interest for the given details is ',SI)


d = float(input('enter the dustance in Km: '))
t = float(input('enter the time taken in minutes: '))
s = d*60/t
print('speed is ',s,'Km/h')


reply = str(input('Do you know the base and height of the Triangle ? yes or no? '))
if reply == 'yes':
    b = float(input('Enter the base of the triangle in metre: '))
    h = float(input('Enter the height of the triangle in metre: '))
    a = 0.5*b*h
    print('Area of the triangle is ',a,'sq m.')
elif reply == 'no':
    x = float(input('Enter 1st side of triangle in m: '))
    y = float(input('enter 2nd side in m: '))
    z = float(input('enter 3rd side in m: '))
    s = (x+y+z)/2
    A = (s*(s-x)*(s-y)*(s-z))**0.5
    print('Area of the triangle is ',A,'sq m.')
else:
    print('please reply yes or no')


a = int(input('enter the cofficient of x^2 :'))
b = int(input('enter the cofficient of x :'))
c = int(input('enter the constant :'))
d = b**2 - 4*a*c
if d < 0:
    print('The roots are not real.')
elif d >= 0:
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print('The roots are ',r1,' ',r2,)


