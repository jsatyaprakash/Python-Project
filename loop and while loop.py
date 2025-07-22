#Program for Generating 1 to N numbers where N is +ve
#WhileLoopEx1.py
n=(int(input("Enter How Many Numbers u want to Generate:")))
#10
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else: 
    print("-"*50)
    print("Number within:{}".format(n))
    print("-"*50)
    i=1 #Initlization part
    while(i<=n): #conditional part
        print("\t{}".format(i))
        i=i+1 #Updation part
    else:
         print("-"*50)
print("other statements in program")
        
#Program for Generating N to 1 numbers where N is +ve
#WhileLoopEx2.py  
n=int(input("Enter How Many Numbers u want Generate:"))
#10
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-"*50)
    i=n #Initlization part
    while(i>=1): #cond part
        print("\t{}".format(i))
        i=i-1 #i-=1 Updation part
    else:
        print("-"*50)
print("other statement in program")     
                  
#Program for Generating N to 1 numbers where N is +ve
#WhileLoopEx3.py
n=int(input("Enter How Many Numbers u want to Generate:"))
#10 
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:    
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-"*50)
    while(n>=1): #cond part
        print("\t{}".format(n))
        n=n-1 # n-=1 Upadation part
    else:
        print("-"*50)
print("other statements in program")                

#Program for Generating all even   numbers where N is +ve
#WhileLoopEx4.py
n=int(input("Enter How Many Even Numbers u want to Generate:")) #10
if(n<=0):
   print("\t{} is Invalid Input".format(n))
else:
   print("-"*50) 
   print("Even Numbers within:{}".format(n))
   print("-"*50)
   i=2 #Initlization part
   while(i<=n): #conditional part
      print("\t{}".format(i))
      i=i+2 #Updation part
   else:
       print("-"*50)
print("other statements in program")        
                          
#Program for Generating all even   numbers where N is +ve
#WhileLoopEx5.py                    
n=(int("Enter How Many Even Numbers u want to Generate:"))#10
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Even Number within:{}".format(n))
    print("-"*50)
    i=1 #Initlization part
    while(i<=n):
        if(i%2==0):
            print("\t{}".format(i))
        i=i+1
    else:
        print("-"*50)          

n=(int("Enter a positive number (n):"))
if(n<=0):
    print("please enter a positive number.")
else:
    print(f"odd numbers from 1 to {n} are:")
    for i in range(1, n+1):
        if i %2 !=0:
            print(i, end='')

# Program to generate even numbers in reverse order within a given range n

# Input from user
n = int(input("Enter a positive number: "))

print("Even numbers in reverse order:")

# Start from n and go down to 2 (inclusive), step -2
for i in range(n, 1, -1):
    if i % 2 == 0:
         print(i,end='')

# Program to generate odd numbers in reverse order within a given range n

# Input from user
n = int(input("Enter a positive number: "))

print("Odd numbers in reverse order:")

# Start from n-1 if n is even, or n if n is odd
start = n if n % 2 != 0 else n - 1

# Loop from start to 0 (exclusive), step -2
for i in range(start, 0, -2):
    print(i,end='')

#for loop  or   for ...else  loop
#Program for generating 1 to N by using for loop  where N is +VE
#ForLoopEx1.py
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("number within:".format(n))
    print("-"*50)
    for i in range(1,n+1):
        print("\t{}".format(i)) 
    else:
        print("-"*50)

#Program for generating N to 1 by using for loop  where N is +VE
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
#n=5
if(n<=0):
    print("{} is Invalid Input".format(n))  
else:
    print("-"*50)
    print("Number from {} to 1".format(n))
    print("-"*50)
    for i in range(n,0,-1):
        print("\t{}".format (i))
    else:
        print("-"*50)

#Program for generating all Even Numbers with for loop  where N is +VE
#ForLoopEx3.py
n=int(input("Enter How Many Even Number u want to generate:")) #n=5
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Even Number within {}".format(n))
    print("-"*50)
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
        print("-"*50)

#Program for generating all Even Numbers with for loop  where N is +VE
#ForLoopEx4.py
n=int(input("Enter How Many odd Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("odd Numbers within {}".format(n))
    print("-"*50)
    for i in range(1,n+1,2):
        print("\t{}".format(i))
    else:
        print("-"*50)

#Program for generating all Odd Numbers with for loop  where N is +VE
#ForLoopEx5.py
n=int(input("Enter How Many odd Numbers u want to generate:")) #n=10
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("List of odd Numbers from {} to 1".format(n))
    print("-"*50)
    if(n%2==0):
        n=n-1
        for i in range(n,0,-2):
            print("\t{}".format(i))
        else:
            print("-"*50)

#Program for generating all Even Numbers with for loop  where N is +VE
#ForLoopEx6.py
n=int(input("Enter How Many Even Numbers u want to generate:")) #n=10
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("List of odd Number from {} to 1".format(n))
    print("-"*50)
    if(n%2!=0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("-"*50)

#Program for Generating Mul Table for Given Number +Ve Number
# by using while Loop and for loop
#ForLoopEx7.py
n=int(input("Enter a Number for Generate Mul Table:"))
if(n>=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*60)
    print("While Loop--Mul table for {}".format(n))
    print("-"*60)
    i = 1
    #While(i<=10):
    print("\t {} x {} = {}".format(n, i, n*i)) 
    i = i + 1
#else:
print("-"*60)
print("for Loop--Mul table for {}".format(n))
print("-"*60)
for i in range(1,11):
    print("\t{} x {} = {}".foramt(n,i,n*i))
else:
    print("-"*60)    

#ForLoopEx8.py
s="PYTHON" # here s is Iterable Object
print("By using while Loop FORWARD DIRECTION with +VE Indices")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
print("By using while Loop FORWARD DIRECTION with -VEIndices")
i=-len(s)
while(i<=-1):
     print("\t{}".format(s[i]))
     i=i+1 
print("BY using while Loop BACKWARD DIRECTION with +VE Indices")
i=len(s)-1
while(i>=0):
    print("\t{}".format(s[i]))
    i=i-1
print("By using while Loop BACKWARD DIRECTION with -VE Indices")
i=-1
while(i>=(-len(s))):
    print("\t{}".format(s[i]))
    i=i-1
else:
    print("-"*50)

#ForLoopEx9.py
s="HYDERABAD" #here s is iterablle object
print("By using for Loop BACKWARD DIRECTION")
for ch in s[::-1]:
      print("\t{}".format(ch))
print("By using for Loop FORWARD DIRECTION with -VE Indices")
for i in range (-len(s),0):
    print("\t{}".format(s[i]))
print("By using for Loop BACKWARD DIRECTION with -VE Indices")
for i in range(-2,-(len(s)+1),-1):
    print("\t{}".format(s[i]))

#program for acceling line of Text and Count number of words
#ForLoopEx10.py
line=input("Enter a Line of Text:")
words=line.split()
print("Given Line of text:",line)
for word in words:
    print("\t{}".format(word))
print("Number of words=",len(words))                  

#program for Finding Factorial of 'N' Natural Nums
# if n>0--------- fact(n)= 1x2x3x4.....xn   OR nxn-1xn-2....x0!
# if n=0--------- fact(0)= 1
# if n<0---------Invalid input
#FactorialEx1.py
n=int(input("Enter a number for cal Factorial:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    fact=1 #Multiplicative Identity
    for i in range(1,n+1):
        fact=fact*i #OR fact *=  i
    else:
        print("factorial({})={}".format(n,fact))

#program for Finding Factorial of 'N' Natural Nums
# if n>0--------- fact(n)=  n x n-1 x n-2....x 0!
# if n=0--------- fact(0)= 1
# if n<0---------Invalid input
#FactorialEx2.py
n=int(input("Enter a Number for cal Factorial:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    fact=1 #Multiplicative Identity
    for i in range(n,0,-1):
    #else:
        print("\t{}!={}".format(n,fact))         

#program for Finding Product of 'N' Natural Nums
#NatNumsProductEx1.py
n=int(input("Enter How Many Natual Nums Sum u Want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    p=1 #Multiplicative Identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p*i #p*=i
    else:
        print("product={}".format(p)) 

#program for Finding Sum of 'N' Natural Nums
#NatSumEx1.py
n=int(input("Enter How Many Natual Nums Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s=0 # Additive Identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i #s+=i
    else:
        print("sum={}".format(s))

#program for Finding Sum of 'N' Natural Nums
#NatSumEx1.py
n=int(input("Enter How Many Natual Nums Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s,ss,cs=0,0,0 #Additive
    print("-"*60)
    print("\tNat Nums\tSquares\t\t\tCubes")
    print("-"*60)
    for i in range(1,n+1):
        print("\t\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+1
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*60)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s, ss , cs))
        print("-"*60)

#program for Finding Sum of Digits of Given Number
#SumOfDigitsEx1.py
n=input("Enter a Number for Finding sum of Its Digits:") #2389
s=0
for d in n: #here n is of type <class, str>
    s=s+int(d) # s+=int(d)
else:
    print("sumofdigits({})={}".format(n,s))    

#program for Finding Sum of Digits of Given Number
#SumOfDigitsEx2.py
n=int(input("Enter a Number forr Finding sum of Its Digits:")) #2389
tn=n
s=0
while(n>0):
    d=n%10
    s=s+d
    n=n//10
else:
    print("SumofDigits({})={}".format(tn,s))
        
