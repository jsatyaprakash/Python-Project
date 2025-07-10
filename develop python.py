a=10
b=20
c=a+b
print(a)
print(b)
print(c)

a=10
b=20
c=a+b
print("----------------------------")
print("val of a=",a)
print("val of b=",b)
print("sum=",c)
print("----------------------------")

#a=float(input("Enter First Value"))
#b=float("val of b={}".format(b))
#print(f"sum={c}")
#print("*"*40)

#ouput statement in python
#syntax-1:print(val1)
a=10
print(a)
a=10
b=20
c=a+b
print(a,b,c)

#syntax-2:print(msg)
       #or
#print(msg1,msg2,....,msg-n)       
#print(msg1+msg2+....+msg-n)
print("Hello python world")
print("Hello","python","World")
print("Hello"+'Python'+"World")
print("Hello"+" "+"Python"+" "+"World")

print("10"+"34")
#print("10"+34) typeerror:can only concatenate str (not "int") to str
print(int("10")+34)
print("10"+str(34))

#syntax:print(massage cum value)
       #or
#print(value cum massage)
a=10
print("val of a=",a)
print("val of a="+str(a))

print(a,"is the val of a")

a=10
b=20
c=a+b
print("sum=",c)
print(c,"is the sum")

a=10
b=20
c=a+b
print("sum of",a,"and",b,"=",c)
print("sum(",a,",",b,")=",c)
print(a,"+",b,"=",c)
print(str(a)+"+"+str(b)+"="+str(c))

#syntax-4:print(Massage cum value with format())
                     #or
#print(value cum Message with format())

a=10
print("val of a={}".format(a))
print("{}is the val of a".format(a))

a=10
b=20
c=a+b
print("sum of{}and{}={}".format(a,b,c))
print("sum({},{}={})".format(a,b,c))
print("{}+{}={}".format(a,b,c))

#syntax-5:print (f"Massage {Var1},{var2},...{var-n}")
a=10
print(f"val of a={a}")
print(f"{a} is the val of a")
a=10
b=20
c=a+b
print(f"sum of {a} and {b}={c}")
print(f"sum ({a},{b})={c}")

#syntax:print("Massage value with format specifiers")
a=10
b=20
c=a+b
print("sum of %d and %d=%d" %(a,b,c))
print("sum of(%d,%d)=%d"%(a,b,c))

#a=1.2
#b=2.3
#c=a+b
#print("sum of %f and %f=%f"%(a,b,c))
#print("sum of %0.2f and %o.2f=%o.2f"%(a,b,c))
#print("sum of %0.10f and $0.10f=%0.10"%(a,b,c))

a=3.456789
print("val of a=%f" %a)
print("val of a=%0.2f" %a)
a=3.455789
print("val of a=%0.2f" %a)
a=3.454789
print("val of a=%0.2f" %a)

#sno=10
#sname="Rossum"
#marks=23.45
#print("My Roll Number is % and name is and marks is %f" %(sno,sname,marks))
#print("My Roll Number is %d and name is '%s' and marks is %0.2" %(sno,sname,marks))

lst=[10,"RS",34.45,True]
print("content of lst={}.format(lst)")
#print("content of lst=%d" %lst) Typeerror:%d foramt :a real number is required, not list
print("content of lst=%s" %str(lst))
d={10:1.2,20:2.3,30:3.4}
print("content of d=%s" %str(d))

#syntax-7:print(value,end="delimter")
for val in range (10,21,2):
    print(val,end='')

#DataReadEx1.py
print("Enter Any Value")
a=input()
print("Val of a={}and type={}".format(a,type(a)))

#DataReadEx2.py
a=input("Enter Any Value:")
print("Val of a={} and type={}".format(a,type(a)))

#DataReadEx3.py
a=input("Enter Any Value:")
print("Val of a={} and type={}".format(a,type(a)))
#conert value of a into float type
b=float(a)
print("val of b={} and Type={}".format(b,type(b)))

#program for Reading any Numerical Vale and multiply them
#DataReadEx4.py
a=input("Enter First Value:")
b=input("Enter First Value:")
#convert 'a' and 'b' into int
x=float(a)
y=float(b)
z=x*y
print("First value={}".format(x))
print("second value={}".format(z))

#program for reading any two Numerical value and Multiply them
#DataReadEx5.py
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=x*y
print("First Value={}".format(x))
print("Second Value={}".format(y))
print("Product={}".format(z))

#program for Reading any Two Numerical value and Multiply them
#DataReadEx6.py
x=float(input("Enter First Value:"))
y=float(input("Enter second Value:"))
print("First Value={}".format(x))
print("Second Value={}".format(y))
print("Product={}".format(x*y))

#program for Reading any Two Numerical Value and Multiply them
#DataReadEx7.py
print("product={}".format(float(input("Enter First Value:"))*float(input("Enter Second Value"))))

#program For Cal Area Of Circle
#DataReadEx8.py
r=(input("Enter Radius:"))
ac=3.14*r*r
print("-*40")
print("\t\tRadius:{}".format(r))
print("\t\tArea of circle:{}".format(ac))
print("---------------------------or--------------------------")
print("\t\tArea of circle:%0.2f" %ac)
print("--------------------------------or---------------------")
print("\t\tArea of circle:{}".format(round(ac,2)))
print("-"*50)

radius = float(input("Enter radius: "))
area = 3.14*radius*radius
print("\t\radius: {}".format(radius))
print("\t\tArea of circle : {}".format(area))

side = float(input("Enter the length of the side of the square: "))
area = side * side
perimeter = 4 * side
print("Area of square: {}".format(area))
print("Perimeter of square: {}".format(perimeter))

radius = float(input("Enter the radius of the circle: "))
perimeter = 2 * 3.14 * radius
print("Perimeter (Circumference) of the circle: {}".format(perimeter))

triangle = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * triangle * height
print("Area of triangle: {}".format(area))

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area of rectangle: {}".format(area))
print("Perimeter of rectangle: {}".format(perimeter))


m=input("Enter the value of m:")
result=3*m
print("the value of 3m is:",result)

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
result = (a + b) ** 2
print("The value of (a + b)^2 is:", result)

a = float(input("Enter the value of a: "))
m = float(input("Enter the value of m: "))
n = float(input("Enter the value of n: "))
result = a**m / a**n
print("The value of a^m / a^n is:", result)

#Program for demonstrating the Functionality of Arithmetic Op
#ArithmeticOpEx1.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
print("-"*50)
print("\t\tArithmetic Operators Result")
print("-"*50)
print("\t\t\t{} + {} = {}".format(a,b,a+b))
print("\t\t\t{} - {} = {}".format(a,b,a-b))
print("\t\t\t{} * {} = {}".format(a,b,a*b))
print("\t\t\t{} / {} = {}".format(a,b,a/b))
print("\t\t\t{} // {} = {}".format(a,b,a//b))
print("\t\t\t{} % {} = {}".format(a,b,a%b))
print("\t\t\t{} ** {} = {}".format(a,b,a**b))
print("-"*50)

#program for Cal simple Interest and total amount to pay
#ArithmeticOpEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter rate of interest:"))
#Cal si and totamt
si=(p*t*r)/100
totamt=p+si
print("*"*50)
print("\tSimple Interest Result")
print("*"*50)
print("\t\tPrinciple Amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of Interest:{}".format(r))
print("\t\tSimple Interest:{}".format(si))
print("\t\tTotal Amount to pay:{}".format(totamt))
print("*"*50)

#program for Cal Square root of any Number without using Pre-Defined Function
#ArithmeticOpEx3.py
n=float(input('Enter a number for cal Square Root:'))
res=n**0.5 # OR  res= n** (1/2)
print("Sqrt({})={}".format(n,res))

#ArithmeticOpEx4.py
wamt=int(input("Ennter How Much Amount u want to withdraw:"))
notes500=wamt//500
wamt=wamt%500
notes200=wamt//200
wamt=wamt%200
notes100=wamt//100
wamt=wamt%100
print("\t\tNumber of 500={}".format(notes500))
print("\t\tNumber of 200={}".format(notes200))
print("\t\tNumber of 100={}".format(notes100))

#program for accepting any two values and swap them (Interchange)
#AssignmentopEx1.py
a,b=input("Enter value of a:"),input("Enter value of b:")
print("------------------------------------------------------")
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("------------------------------------------------------")
a,b=b,a #Multi Line assignment
print("\tswapped value of a=".format(a))
print("\tswapped value of b={}".format(b))
print("------------------------------------------------------")

#program for accepting any Two values and swap them(Intecrchange)
#AssignmentopEx2.py
a,b=input("Enter value of a:"),input("Enter value of b:")
print("-----------------------------------------------------------")
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("------------------------------------------------------------")
t=a #single Line assigment
a=b
b=t
print("\tswapped value of a={}".format(a))
print("\tswapped value of b={}".format(b))
print("-------------------------------------------------------------")

#program for accepting any Two Numerical Integer Values and swap them (Interchange)
#AssigmentopEx3.py
a,b=int(input("Enter value of a={}".format(a)))
print("-----------------------------------------------------")
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("-----------------------------------------------------")
a=a+b
b=a-b
a=a-b
print("\tswapped value of a={}".format(a))
print("\tswapped value of b={}".format(b))
print("-----------------------------------------------------")

#program for accepting any Two Numerical Integer values and swap them (Interchange)
#AssignmentopE4.py
a,b=int(input("Enter value of a:")),int(input("Enter value of b:"))
print("------------------------------------------------------------")
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("------------------------------------------------------------")
a=a*b
b=a//b
a==a//b
print("\tswapped value of a={}".format(a))
print("\tswapped value of b={}".format(b))
print("-------------------------------------------------------------")

#program for accepting any Two Numerical Integer values and swap them (Interchange)
#AssignmentopEx.py
a,b(input("Enter value of a={}".format(a)))
print("----------------------------------------------------------------")
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("----------------------------------------------------------------")
a=a^b #Bitwise XOR(^)
b=a^b
a=a^b
print("\tswapped value of a={}".format(a))
print("\tswapped value of b={}".format(b))
print("----------------------------------------------------------------")

#program for demobstarting the functionality of Relational op
#RelationalopEx.py
a=float(input("Enter First Value:"))
b=float(input("Enter second value:"))
print("-"*50)
print("\tResults of Relational operators")
print("-"*50)
print("\t\t{}>{}={}".format(a,b,c,a>b))
print("\t\t{}<{}={}".format(a,b,a<b))
print("\t\t{}=={}={}".format(a,b,a==b))
print("\t\t{}!={}={}".format(a,b,a!=b))
print("\t\t{}>={}={}".format(a,b,a>=b))
print("\t\t{}<={}={}".format(a,b,a<=b))
print("-"*50)

#logical operators
#'and' operator
True and False 
False and True
False and False
True and True

10>20 and 30>20
10>20 and 30>20 and 30>40
10>2 and 20>3 and 40>30
10>2 and 30>40 and 40>20

#short circuit Evaluation in the case of 'and' operator
100 and 200
-123 and 123
123 and 0
123 and 234 and 145
False and 123 and True 
-12 and 0b000 and 234
"PYTHON" and "DSA" and "C"
"False" and "True"
"" and "$"

#'or' operator
True or False
False or True
False or False
False or True

10>2 or 20>30
20>10 or 30>40 or 50>60
10>20 or 40>50 or 50>30
20>30 or 30>40 or 40>50

#short circuit Evaluation in case of 'or' operator
10 or 20
10 or 0
0 or 20
10 or 30 or 40
"PYTHON"  or "Java" or  "c"
10 or 20 and 30
20 and 30 or 40
20 or 40 and 50 or 60
"PYTHON" or "Java" and "c" or "HTML"

#'not' operator
not True
not False

10>20 and 30>20
not(10>20 and 30>20)
20>10 or 30>20
not(20>10 or 30>20)

not 20
not 0
not 123
not "PYTHON"
not 0b0000
not 10-11
not "not"
not "False"
not(not(bool(123)))

#Bitwise left shift operator(<<)
a=10
b=a<<3
print(b)
print(4<<2)
print(9<<2)
print(10<<0)
#print(10.3<<2) typeError:unsupported oprand type(s) for<<:'float' and 'int'
#print(4<<-1) valueError:negative shift count
 
 #Bitwise Rightshift operator(>>)
a=10
b=a>>3
print(b)
print(16>>2)
print(32>>3)
print(32>>2)
print(32>>0)
#print(80.5>>4) typeErroe:unsupported operand type(s)<<:'float' and 'int'
#print(42>>-4) valueError:negative shift count

#Bitwise And(&)
1 & 0
0 & 1
0 & 0
1 & 1

a=5
b=5
c=a&b

print(4&3)
print(10&15)
4 & 3
"Python" and "Java"
#"Python" & "Java" typeError:unsupported operand type(s) for &:'str'
1.2 and 1.5
1.5
#0.2 & 1.5 TypeError: unsupported operand type(s) for &: 'float' and 'float'

s1={10,20,30}
s2={30,40,50}
s3=s1.intersection(s2)
print(s3,type(s3))
s1={10,20,30}
s2={30,40,50}
s3=s1&s2 #Bitwise AND(&)
print(s3,type(s3))
{10,20,30}&{15,25,35}

s1={1.2,2.3,4.5}
s2={2.3,4.5,5.6}
s1=s1&s2 #Bitwise AND(&)
print(s3,type(s3))
{'Mango','Kiwi',}&{'Mango','sberry'}

#[10,20,30]&[110,120,130] typeError:unsupported operand type(s) for &: 'list' and 'list'
set([10,20,30])&set([110,120,130])
a={10,20,30}
b={15,30,45}
a and b
set ("RADRA") & set ("RANDSON")

#Bitwise oR (|)
1 | 0
0 | 1
0 | 0
1 | 1

a=4
b=3

c=a|c
print(c)

a=10
b=10
c=a|b
print(c)

a=15
b=3
print(a|b)

a={10,20,30}
b={15,30,45}
c=a.union(b)
print(c,type(c))

a={10,20,30}
b={15,30,45}
c=a|b
print(c,type(c))
{"Rohit","Virat","Rossum"} | {"Travis","Rossum"}
{1.2,2.3,4.5}|{4.5,5.6,6.7,"Python"}

a={10,20,30}
b={15,30,45}
a or b

#Bitwise complement operator(~)
a=10
~a
a=123
~a
a=-100
#~a=1.3
#~a=1.3 TypeError:bad operand type for unary ~'float'

#Internal Flow of Bitwise Complement Operator ( ~ )
a=10
~a

#Internal Flow of Bitwise Complement Operator ( ~ )
a=15
~a

#Bitwise  XOR Operator ( ^ )
1^0
0^1
0^0
1^1

a=2
b=3
c=a^b
print(c)
print(10^15)
print(345^345)

{1.2,3.4,4.5}^{4.5,1.2,3.4}
#"RADAR" ^ "ABRAKADABAR" TypeError:unsupported operand type(s) for ^: 'str' and 'str'
set ("RADAR") ^ set ("AMRAKADABRA")
#1.2^2.3 TypeError: unsupported operand type(s) for ^: 'float' and 'float'

#Membership Operators
#in operator
#not in operator
s="PYTHON" 
"p" in s
"k" in s
"No" in s
"No" in s
"No" in s[::-1]
"NO" not in s[::-1]
"PYT" in s
"PTO" in s
"PTO" in s[::2]
lst=[100,"ROSSUM",23.45,2+3j]
100 in lst
"ROS" in lst
"ROS" in lst[1]
#2+3j in lst[-1] TypeError: argument of type 'complex' is not iterable
#2.0 in lst[-1].real TypeError: argument of type 'float' is not iterable
"muss" in lst[1][::-1]

#Short hand Operators
bal=5000
damt=6000
bal += damt #Normal Expression
print(bal)

bal=5000
damt=6000
bal += damt #Here += is called Short hand  Operator
print(bal)

a=10
b=5
a=a*b
print(a)

a=10
b=5
a=a*b # Here *= is called Short hand  Operator
print(a)

a=10
b=2
a=a-b
print(a)

a=10
b=2
a-=b
print(a)

a=2
b=3
c=4
a=a+b*c
print(a)

a=2
b=3
c=4
a+=b*c
print(a)

#Normal Expression
#is Operator
#is not Operator
lst1=[10,"RS",23.45]
print(lst1,id(lst1))

lst2=lst1 #deep copy
print(lst2,id(lst2))

lst1 is lst2
lst1 is not lst2

lst1=[10,"RS",23.45]
print(lst,id(lst1))

lst2=lst1.copy()
print(lst2,id(lst2))

lst1 is lst2
lst is not lst2

#Ternary Operator in Python
#Program for Accepting a Value and Decide whether It is Palindrome or not
#TernaryOpEx1.py
value=input("Enter value:") #value=PYTHON
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("{} is {}".format(value,res))

#Program for accepting Two Numerical values and find Big among them and check for equlity.
#TernaryOpEx2.py
a=float(input("Enter value of a:")) #a=20
b=float(input("Enter value of b:")) #b=20
bv=a if a>b else b if b>a else "Both values are Equal"
print("Big({},{})={}".format(a,b,bv))

#Program for accepting Three Numerical values and find Big among them and check for equlity.
#TernaryOpEx3.py
a=float(input("Enter value of a:")) #a=20
b=float(input("Enter value of b:")) #b=20
c=float=(input("Enter value of c")) #c=20
bigv=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All values are Equal"
print("Big({},{},{})={}".format(a,b,c,bigv))

#Program for accepting Three Numerical values and find Big among them and check for equlity.
#TernaryOpEx4.py
a=float(input("Enter value of a:")) #a=20
b=float(input("Enter value of c:")) #b=20
c=float(input("Enter value of c:")) #c=20
bigv=a if b<=a>c else b if a<b>=c else c if a<=c>b else "All values are Equal"
print("Big{},{},{})={}".format(a,b,c,bigv))

#Program for accepting Any Numerical values and decide whether It is +Ve or -Ve or Zero
#TernaryOpEx5.py
value=float(input("EnterAny value:"))
res="Zero" if value==0 else "+VE" if value>0 else "-VE"
print("{} is {}".format(value,res))
