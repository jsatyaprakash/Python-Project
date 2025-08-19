#Program for accepting List of of Line of Text and Display their word and length
#DictCompEx1.py
line=input("Enter Line of Text:")
d={word:len(word)  for word in line.split() }
print(d)

#Program for accepting List of of Line of Text and Display their word and length
#DictCompEx1.py
line=input("Enter Line of Text:")
d={word:len(word)  for word in line.split() if len(word) in range(3,6) }
print(d)

#Program for accepting List of Values and Separate Positive and Negative Values
#ListCompEx1.py
lst=[10,-20,30,-40,-50,60,70,0,25]
pslist=[val for val in lst  if val>0] # List Comprehension
nglist=[val for val in lst  if val<0] # List Comprehension
print("List of +VE Values=",pslist)
print("List of -VE Values=",nglist)

#Program for accepting List of Values and Separate Positive and Negative Values
#ListCompEx2.py
n=int(input("Enter How Many Values u want to read :"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Values")
        print(lst)
        pslist = [val for val in lst if val > 0]  # List Comprehension
        nglist = [val for val in lst if val < 0]  # List Comprehension
        print("List of +VE Values=", pslist)
        print("List of -VE Values=", nglist)

#Program for accepting List of Values and Separate Positive and Negative Values
#ListCompEx3.py
print("Enter List of Values separated by Comma:")
lst=[float(val)  for val in input().split(",")]
print("List of Elements")
print(lst)
pslist = [val for val in lst if val > 0]  # List Comprehension
nglist = [val for val in lst if val < 0]  # List Comprehension
print("List of +VE Values=", pslist)
print("List of -VE Values=", nglist)

#Program for accepting List of Values and get Positive Values
#ListCompEx4.py
print("Enter List of Values separated by space:")
lst=[float(val)  for val in input().split()  if  float(val)>0]
print("List of +VE Elements")
print(lst)

#Program for accepting List of Values and get Negative Values
#ListCompEx4.py
print("Enter List of Values separated by space:")
lst=[float(val)  for val in input().split()  if  float(val)<0] # List Comprehension
print("List of -VE Elements")
print(lst)

#Program for accepting List of Values and Separate Positive and Negative Values
#NotTupleCompEx.py
tpl=(10,-20,30,-40,-50,60,70,0,25)
pstpl=(val for val in tpl  if val>0) # It is not tuple Comprehension--It build <class, generator>
#Convert generator Object into tuple object
pstpl1=tuple(pstpl)
print(pstpl1)

#Program for accepting set of Values and get Multiples of 3
#SetCompEx1.py
print("Enter Set of Values Separated by Space:")
stvals={float(val) for val in input().split()  if (float(val)>0 and float(val)%3==0) }
print("Set of Multiple of 3")
print(stvals)

#Program for accepting set of Values and get Primes
#SetCompEx1.py
def isprime(n):
    result=True
    for i in range(2, n):
        if (n % i == 0):
            result = False
            break
    return result
#Main Program
print("Enter Set of Values Separated by Space:")
stvals={int(val) for val in input().split()  if isprime(int(val)) and int(val)>=2 }
print("Set of Primes")
print(stvals)

#Program for Computing Sum of Two Numbers By using Anonymous Functions
#AnonymousfunEx1.py
sumop=lambda a,b: a+b

#Main Program
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
res=sumop(a,b)
print("Sum({},{})={}".format(a,b,res))

#Program for accepting To Valaues and Find Biggest among them
#AnonymousfunEx2.py
findmax=lambda x,y: x if x>y else y if y>x else "Both Values are equal"

#main Program
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
res=findmax(a,b)
print("max({},{})={}".format(a,b,res))

#Program for accepting List of Valaues and Find Biggest among them
#AnonymousfunEx3.py
findmax=lambda lstobj:max(lstobj)
findmin=lambda lstobj:min(lstobj)

#main Program
print("Enter List of Values Separated by Space")
lst=[float(val) for val in input().split()]
bv=findmax(lst)
sv=findmin(lst)
print("Max({})={}".format(lst,bv))
print("Min({})={}".format(lst,sv))

#Program for accepting set of Values and get Primes
#AnonymousfunEx4.py
def prime(n): # Normal Function Definition
    result=True
    for i in range(2, n):
        if (n % i == 0):
            result = False
            break
    if(result):
        return n
    else:
        return "Not_Prime"
#Anonymous function
findprime=lambda n:prime(n)

#Main Program
print("Enter Set of Values Separated by Space:")
lst=[int(val) for val in input().split() if int(val)>=2] # lst=[2,5,6,9,7,12,13]
primelist=[]
for val in lst:
    pn=findprime(val)
    if(type(pn)==int):
        primelist.append(pn)
else:
    print("List of Primes")
    print(primelist)

#Program for accepting a word and sort Those Letters
#AnonymousfunEx5.py
sortwordletters=lambda word:"".join(sorted(word))
#main Program
word=input("Enter Any Word:")
sv=sortwordletters(word)
print("Sorted Values in word in ascending Order=",sv)
print("Sorted Values in word in decending Order=",sv[::-1])

#program for Finding Number of Occurences of Values in in List
#lst=[10,20,10,20,30,40,50,10]
#Expected Ouput: {10:3, 20:2,30:1,40:1,50:1}
#NumberOfOccurences.py
def findoccurences(lst): # lst=[10,20,10,20,30,40,50,10]
    if(len(lst)==0):
        print("List is empty")
    else:
        d={} # empty Dict
        for val in lst:
            if val not in d:
                d[val]=1
            else:
                d[val]=d[val]+1
        else:
            for k,v in d.items():
                print("\t{}-->{}".format(k,v))

#main program
print("Enter Set of Values Separated by Space:")
lst=[float(val) for val in input().split() ] # lst=[10,20,10,20,30,40,50,10]
findoccurences(lst) # Function call

#Special Functions in Python
#program for accepting List of Values and Get +Ve Values by using filter()
#FilterEx1.py
def pos(n): #Normal function
    if(n>0):
        return True
    else:
        return False
#main program
print("Enter List of values separated by space:")
lst=[float(val) for val in input ().split()]
print("content of lst=",lst) #10 20 -30 40 50 -60 -12 34 5 -9 0
#use filter() to ge +vals
x=filter(pos,lst) # here x is an object of <class,'filter'>
#Type cast filter object into list / tuple/set...etc
pslist=list(x)
print("+ve Elements=",pslist)

#program for accepting List of Values and Get +Ve Values by using filter()
#FilterEx2.py
def pos(n):
   return n>0
def neg(n):
   return n<0
#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
print("Content of lst=",lst) # 10 20 -30 -40 50 -60 -12 34 5 -9 0
#use filter() to ge +vals
pslist=tuple(filter(pos,lst)) # Here x is an object of <class, 'filter'>
nglist=tuple(filter(neg,lst)) # Here x is an object of <class, 'filter'>
print("+Ve Elements=",pslist)
print("-Ve Elements=",nglist)

#program for accepting List of Values and Get +Ve Values by using filter()
#FilterEx3.py
pos=lambda n: n>0
neg=lambda n: n<0

#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
print("Content of lst=",lst) # 10 20 -30 -40 50 -60 -12 34 5 -9 0
#use filter() to ge +vals
pslist=tuple(filter(pos,lst)) # Here x is an object of <class, 'filter'>
nglist=tuple(filter(neg,lst)) # Here x is an object of <class, 'filter'>
print("+Ve Elements=",pslist)
print("-Ve Elements=",nglist)

#program for accepting List of Values and Get +Ve Values by using filter()
#FilterEx3.py
pos=lambda n: n>0
neg=lambda n: n<0

#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
print("Content of lst=",lst) # 10 20 -30 -40 50 -60 -12 34 5 -9 0
#use filter() to ge +vals
pslist=tuple(filter(pos,lst)) # Here x is an object of <class, 'filter'>
nglist=tuple(filter(neg,lst)) # Here x is an object of <class, 'filter'>
print("+Ve Elements=",pslist)
print("-Ve Elements=",nglist)

#program for accepting List of Values and Get +Ve Values by using filter()
#FilterEx4.py
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
print("Content of lst=",lst) # 10 20 -30 -40 50 -60 -12 34 5 -9 0
#use filter() to ge +vals
pslist=tuple(filter(lambda n: n>0,lst)) # Here x is an object of <class, 'filter'>
nglist=tuple(filter(lambda n: n<0,lst)) # Here x is an object of <class, 'filter'>
print("+Ve Elements=",pslist)
print("-Ve Elements=",nglist)

#program for accepting List of words and Get Only Panlindrome Words
#FilterEx5.py
print("Enter List of Words Separated by Comma:")
words=[word for word in input().split(",")]
print("List of Words")
print(words)
palwords=list(filter(lambda word:word==word[::-1],words))
print("List of Palindrome Words")
print(palwords)

#MapEx1.py
def hike(sal):
    return(sal+sal*50/100)

#Main Program
print("Enter List Of Old Salaries")
oldsals=[float(sal) for sal in input().split() if float(sal)>0]
x=map(hike,oldsals) # Here x is an object of <class, 'map'>
#Type Cast Map Object in List / tuple/set
newsals=list(x)
print("-"*50)
print("\tOld Salary\t\tNew Salary")
print("-"*50)
for old,new in zip(oldsals,newsals):
    print("\t{}\t\t\t\t{}".format(old,new))
print("-"*50)

#MapEx2.py
hike=lambda sal:sal+sal*50/100
#Main Program
print("Enter List Of Old Salaries")
oldsals=[float(sal) for sal in input().split() if float(sal)>0]
newsals=list(map(hike,oldsals))
print("-"*50)
print("\tOld Salary\t\tNew Salary")
print("-"*50)
for old,new in zip(oldsals,newsals):
    print("\t{}\t\t\t\t{}".format(old,new))
print("-"*50)

#MapEx3.py
print("Enter List Of Old Salaries")
oldsals=[float(sal) for sal in input().split() if float(sal)>0]
newsals=list(map(lambda sal:sal+sal*50/100,oldsals))
print("-"*50)
print("\tOld Salary\t\tNew Salary")
print("-"*50)
for old,new in zip(oldsals,newsals):
    print("\t{}\t\t\t\t{}".format(old,new))
print("-"*50)

#MapEx4.py
print("Enter List of Values for First List Separated by Comma")
x=[float(val) for val in input().split(",")]
print("Enter List of Values for Secoond List Separated by Comma")
y=[float(val) for val in input().split(",")]
z=list(map(lambda a,b:a+b, x,y))
print("-"*50)
print("\tFirst List\t\tSecond List\t\tSum List")
print("-"*50)
for old,new,res in zip(x,y,z):
    print("\t{}\t\t\t\t{}\t\t\t\t{}".format(old,new,res))
print("-"*50)

#MapEx4.py
print("Enter List of Values for First List Separated by Comma")
x=[float(val) for val in input().split(",")]
print("Enter List of Values for Secoond List Separated by Comma")
y=[float(val) for val in input().split(",")]
if(len(x)>len(y)):
    for i in range(len(x)-len(y)):
        y.append(0.0)
elif(len(y)>len(x)):
    for i in range(len(y)-len(x)):
        x.append(0.0)
#Add Multiple List values
z=list(map(lambda a,b:a+b, x,y))
print("-"*50)
print("\tFirst List\t\tSecond List\t\tSum List")
print("-"*50)
for old,new,res in zip(x,y,z):
    print("\t{}\t\t\t\t{}\t\t\t\t{}".format(old,new,res))
print("-"*50)

