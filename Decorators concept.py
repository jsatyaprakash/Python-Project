#Program for Demonstrating the need of Decorators
#DecEx1.py
def square(kvr): # Outer Function--Decorator
	def calculate(): # Inner Function 
		n=kvr() # Calling Normal Formal with Its Formal Param
		res=n**2 # here 'res' is local var to inner function
		return n,res
	return calculate

def  getval():  # Defined by KVR---Normal Function
	return float(input("Enter any Numerical value:"))

#Main Program
calc=square(getval) # This Function call Takes Normal Function Name as argument--Decorator Call

res=calc() # here res is an object of <class, tuple>
print("Square({})={}".format(res[0],res[1]))

#Program for Demonstrating the need of Decorators
#DecEx2.py
def square(gv):  # Here gv is called formal Parameter to getval--Outer Function--Decorator
	def calculate(): # Inner Function
		n=gv()
		res=n**2
		return n,res
	return calculate

@square
def  getval():  
	return float(input("Enter any Numerical value:"))

#Main Program
num,res=getval() # Normal Function 
print("Square({})={}".format(num,res))

#Program for Demonstrating the need of Decorators
#DecEx3.py
def squareroot(calc):
	def processval():
		num,sqv=calc()
		sqrtv=num**0.5
		return num,sqv,sqrtv
	return processval

def square(gv):  # Here gv is called formal Parameter to getval--Outer Function--Decorator
	def calculate(): # Inner Function
		n=gv()
		res=n**2
		return n,res
	return calculate

@squareroot
@square
def  getval():  
	return float(input("Enter any Numerical value:"))

#Main Program
num,sqv,sqrtv=getval() # Normal Function 
print("Square({})={}".format(num,sqv))
print("SquareRoot({})={}".format(num,sqrtv))

#Program for Demonstrating the need of Decorators
#DecEx4.py
def cube(pcval):
	def calculate():
		num,sqv,sqrtv=pcval()
		cbv=num**3
		return num,sqv,sqrtv,cbv
	return calculate

def squareroot(calc):
	def processval():
		num,sqv=calc()
		sqrtv=num**0.5
		return num,sqv,sqrtv
	return processval

def square(gv):  # Here gv is called formal Parameter to getval--Outer Function--Decorator
	def calculate(): # Inner Function
		n=gv()
		res=n**2
		return n,res
	return calculate

@cube
@squareroot
@square
def  getval():  
	return float(input("Enter any Numerical value:"))

#Main Program
num,sqv,sqrtv,cbv=getval() # Normal Function 
print("Square({})={}".format(num,sqv))
print("SquareRoot({})={}".format(num,sqrtv))
print("Cube({})={}".format(num,cbv))

#Program for accepting a Line of Text and Convert into Lower and Upper Case Completely by using Decorator
#DecEx5.py
def lowerconvert(conv):
	def convertproc():
		line,uc=conv()
		lc=line.lower()
		return line,uc,lc
	return convertproc

def upperconvert(gtv):
	def converstion():
		line=gtv()
		uc=line.upper()
		return line,uc
	return converstion


@lowerconvert
@upperconvert
def gettextval():
	return input("Enter Line of Text:")


#Main Program
line,uc,lc=gettextval()
print("Given Line=",line)
print("Upper Case Data=",uc)
print("Lower Case Data=",lc)

#Program for accepting a Line of Text and Convert into Lower and Upper Case Completely by using Decorator
#DecEx6.py
def lowerconvert(conv):
	def convertproc():
		line,uc=conv()
		lc=""
		for ch in line:
			if ord(ch) in range(65,91):
				lc=lc+chr(ord(ch)+32)
			else:
				lc=lc+ch
		return line,uc,lc
	return convertproc

def upperconvert(gtv):
	def converstion():
		line=gtv()
		uc=""
		for ch in line:
			if ord(ch) in range(97,123):
				uc=uc+chr(ord(ch)-32)
			else:
				uc=uc+ch
		return line,uc
	return converstion

@lowerconvert
@upperconvert
def gettextval():
	return input("Enter Line of Text:")


#Main Program
line,uc,lc=gettextval()
print("Given Line=",line)
print("Upper Case Data=",uc)
print("Lower Case Data=",lc)

#Program for Demonstrating the need of Decorators
#Non-DecEx1.py
def  getval():  # Defined by KVR
	return 5
def  square():							#Rama Kant Sir give Square of 5
	n=getval()
	res=n**2
	print("Square({})={}".format(n,res))
def squareroot():							#Shahil Sir give Square Root of 5
	n=getval()
	res=n**0.5
	print("SquareRoot({})={}".format(n,res))
def cube():							#Shaoo give cube  of 5
	n=getval()
	res=n**3
	print("Cube({})={}".format(n,res))

#Main Program
square()
squareroot()
cube()

#Closure in Python
#program for Demonstrating the need of Closure
#ClosureEx1.py
def  grandparent(gpname): # Outer Function
	print("I am from Outer Function")
	def child(cdname): # inner Function---- Closure
		print("Inner Fun:Hi Grand Parent:{}".format(gpname))
		print("\tChild Name:{}".format(cdname))
	return child

#main Program
childval=grandparent("Sr.Rossum") # Outer Function Call
childval("Rossum1") # Inner Function Call
childval("Rossum2") # Inner Function Call
childval("Rossum3") # Inner Function Call

#program for Demonstrating the need of Closure
#ClosureEx2.py
def  grandparent(gpname): # Outer Function
	print("I am from Outer Function")
	def child(cdname): # inner Function---- Closure
		print("Inner Fun:Hi Grand Parent:{}".format(gpname))
		print("\tChild Name:{}".format(cdname))
	child("Rossum1")
	child("Rossum2")
	child("Rossum3")

#main Program
grandparent("Sr.Rossum") # Outer Function Call

#program for Demonstrating the need of Closure
#ClosureEx3.py
def  simpleint(R=8.2): # Outer Function-  OR --Containing Function
	def  siopration(P,T): # Inner Function--Closure (Contained Function)
		si=(P*T*R)/100
		totamt=P+si
		print("-"*50)
		print("Simple Interest Operations")
		print("-"*50)
		print("\tPrinciple Amount=",P)
		print("\tTime=",T)
		print("\tRate of Interest=",R)
		print("\tSimple Interest=",si)
		print("\tTotal Amount to Pay=",totamt)
		print("-"*50)
	return siopration

#Main Program
siop=simpleint() # Outer Function Call
siop(1000,2)
siop(2000,3)
siop(8000,6)

#program for Demonstrating the need of Closure
#ClosureEx4.py
def operation(x): # Outer Function--here x is called Formal Param
	y=1  # Here y is called Local Var in Outer Function and global var for calculation()
	def  calculation(z): # Inner Function--here z is called Formal Param
		res=x+y+z
		print("x={},y={},z={},sum={}".format(x,y,z,x+y+z))
	return calculation

#main Program
calc=operation(5)
calc(10)
calc(15)
calc(6)


#program for Demonstrating the need of Closure
#ClosureEx5.py
y1=1000 # here y1 is called global variable
def operation(x): # Outer Function--here x is called Formal Param
	y=1  # Here y is called Local Var in Outer Function and global var for calculation()
	def  calculation(z): # Inner Function--here z is called Formal Param
		global y1
		nonlocal y
		res=x+y+z+y1
		print("y1={}, x={},y={},z={},sum={}".format(y1,x,y,z,x+y+z))
		y=y+1 # Here we modifying the global var of Inner function and Local of Outer function
		y1=y1+1
	return calculation

#main Program
calc=operation(5)
calc(10)
calc(15)
calc(6)

#generator in python
#Program for Demobstrating the Need of Generators
#GenEx1.py
def kvrrange(Val):
	i=1
	while(i<=Val):
		yield i
		i=i+1

#Main Program
r=kvrrange(6) # Function Call--gives the values only on demand
#here 'r' is an object of <class 'generator'>
#To get the Value from Generator--we use function next()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
#print(next(r))----Gives StopIteration error

#Program for Demonstrating the Need of Generators
#GenEx2.py
def kvrrange(Val):
	i=1
	while(i<=Val):
		yield i
		i=i+1

#Main Program
r=kvrrange(6) # Function Call--gives the values only on demand
#here 'r' is an object of <class 'generator'>
#To get the Value from Generator--we can use for loop
for val in r:
	print(val)

#Program for Demonstrating the Need of Generators
#GenEx3.py
def kvrrange(BVal,EVal):
	while(BVal<=EVal):
		yield BVal
		BVal=BVal+1

#Main Program
r=kvrrange(10,20) # Function Call--gives the values only on demand
print(next(r))
print(next(r))
for val in r:
	print(val)
print("------------------------------------------")
r1=kvrrange(100,110) # Function Call--gives the values only on demand
print(next(r1))
print(next(r1))
for val in r1:
	print(val)

#Program for Demonstrating the Need of Generators
#GenEx4.py
def kvrrange(Beg,End=1,Step=1):
	if(Beg>End):
		End=Beg
		Beg=1
	while(Beg<=End):
		yield Beg
		Beg=Beg+Step

#Main Program
go1=kvrrange(10)
for val in go1:
	print(val)
print("--------------------------------------------------")
go2=kvrrange(10,21)
for val in go2:
	print(val)
print("--------------------------------------------------")
go3=kvrrange(10,21,2)
for val in go3:
	print(val)
print("--------------------------------------------------")
