#Q1
X = int(input())
Y = int(input())
H = int(input())
area = ((X+Y)/2) * H
print("Area of trapezoid is ",area)



#Q2
#first q

w=float(input("enter the weight(in kg):"))
h=float(input("enter the height(in M):"))
BMI=w/(h**2)
print("body mass index is",BMI)

#second q

w=float(input("enter the weight(in Pound):"))
h=float(input("enter the height(in Inches):"))
BMI=(w/0.45)/((h/39.3)**2)
print("body mass index is",BMI)



#Q3
A = int(input()) 
B = int(input())
C = int(input())
if(A+B<C or B+C<A or C+A<B):
    print('Not a Triangle')
else:
    print('A triangle')



#Q4
xyz=int(input("enter three digit no.:"))
ones = xyz % 10
tens = (xyz% 100) // 10
hundreds = (xyz % 1000) // 100
sum=ones+tens+hundreds
print("sum of three digits is:",sum)
if sum % 3==0:
  print("number is divisible by 3")
else:
  print("number is not divisible by 3")



#Q5
digit=int(input("enter the 5 digit no:"))
t=(digit%10)//1
i=(digit%100)//10
g=(digit%1000)//100
i_1=(digit%10000)//1000
d=(digit%100000)//10000
if (d==t and i==i_1 and g==g):
  print("entered no. is palindrome")
else:
  print("entered no. is not palindrome")



#Q6
print("enters numbers will be swap the value".swapcase().center(100))
x=input("Enter the first value(A):")
y=input("Enter the second value(B):")
A=y
B=x
print("A is",A)
print("B is",B)



#Q7
x=int(input("enter the real part of first cmplex no.:"))
y=int(input("enter the imaginary part of first cmplex no.:"))
x_1=int(input("enter the real part of second cmplex no.:"))
y_1=int(input("enter the imaginary part of second cmplex no.:"))
com_1=complex (x,y)
com_2=complex(x_1,y_1)
print(com_1+com_2)
print(com_1*com_2)



#Q8
salary=float(input("enter yours basic salary:"))
HRD=salary*(20/100)
TA=salary*(5/100)
DA=salary*(10/100)
GROSS_SALARY=salary+HRD+TA+DA
print("your GROSS SALARY is equal to",GROSS_SALARY)


#Q9
salary=float(input("enter yours gross salary:"))
if(salary<0):
  print("enter correct gross income")
elif (salary<300000):
  print("there is no income tax on it")

elif(salary>=300000 and salary<1000000):
  y=salary*(10/100)
  print("income tax on you salary is 10% so payable amount in tax is",y)

elif(salary>=1000000 and salary<2500000):
  z=salary*(20/100)
  print("income tax on you salary is 20% so payable amount in tax is",z)
elif (salary>=2500000):
  p=salary*(30/100)
  print("income tax on you salary is 30% so payable amount in tax is",p)

else:
  print("enter correct gross income")


#Q10
x=float(input("Enter the first number="))
y=float(input("Enter the second number="))
z=float(input("Enter the third number="))
if x>=0 and y>=0 and z>=0:
    if x>y and x>z:
        print(x,"is the largets number")
    if y>x or y>z:
        print(y,"is the largest number")
    else:
        print(z,"is the largets number")
elif x<0 and y<0 and z<0:
    if x>y and x>z:
        print(x,"is the largets number")
    if y>x or y>z:
        print(y,"is the largest number")
    else:
        print(z,"is the largets number")
else:
    print("Enter the right number,Please")


#Q11
print("cheak the number is armstrong number is or not".title().center(50))
digit=(input("Enter the 3 digit number:"))
y=int(digit)
count=0
x=len(digit)
if y>=0:
  if x==1:
    print("Entered the three digit no.")
  elif (x==2):
    print("enter the 3 digit no.")
  elif (x==3):
    once=(y%10)
    tense=(y%100)//10
    hund=(y%1000)//100
    if y==((once**x)+(tense**x)+(hund**x)):
      print("Entered number is Armstrong number",y)
    else:
      print("this no. is not a armstrong no.")
  else:
    print("please try again")
else:
  print("enter the valid")


