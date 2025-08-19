#Program for Demonstrating the need of break keyword / statement
#BreakStmtEx1.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of loop")
print("------------------------------")
#--------------------------------
#Requirement:Want to display PYTH without using Indexing and slicing  
for ch in s: #s="PYTHON"
    if(ch=="o"):
        break
    print(ch,end="")
else:
    print("else part of for loop")
print("\nother statements in python")

#Program for Demonstrating the need of break keyword / statement
#BreakStmtEx2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of while loop") 
print("------------------------------") 
#-------------------------------
#Requirement:Want to display PYTH without using Indexing and slicing
i=0
while(i<len(s)): #s="PYTHON"
   if(s[i]=="o"):
      break
   print(s[i],end="")
   i=i+1
else:
    print("else part of while loop")
print("\nother statements in python")

#Program for Demonstrating the need of break keyword / statement
#BreakStmtEx3.py
s="MISSISSIPPI"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("----------------------------------")    
#------------------------------------
#Requriement:Want to display MISS without using Indexing and slicing
ctr=0
for ch in s: #s="MISSISSIPPI"
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
        print(ch,end="")
else:
    print("else part of for loop")
print()
print("other statement in program")

#Program for Demonstrating the need of break keyword / statement
#BreakStmtEx4.py
s="MISSISSIPPI"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of while loop")
print("---------------------------------------")        
#------------------------------------------
#Requirement:Want to display MISS without using Indexing and slicing
ctr=0
i=0
while(i<len(s)): #s="MISSISSIPPI"
    if(s[i]=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
        print(s[i],end="")
        i=i+1
    else:
        print("else part of while loop")
    print()
    print("other statements in program")

#Program for accepting a Number and decide whether It is Prime or Not
#BreakStmtEx5.py
n=int(input("Enter a number:"))
if(n<=1):
    print("\t{} is Invalid input".format(n))
else:
    result="PRIME"
    for i in range(2,n):
        if(n%i==0):
            result="NOT PRIMS"
            break
    print("{}".format(n,result))

#Program for accepting a Number and decide whether It is Prime or Not
#BreakStmtEx6.py
n=int(input("Enter a Number"))
if(n<=1):
    print("\t{} is Invalid input".format(n))
else:
    result=True
    for i in range(2,n):
        if(n%i==0):
            result=False
            break
    res="PRIME" if result else "NOT PRIME"
    print("\t{} is {}".format(n,res))

#Program for accepting a word  and decide whether It is Vowel word or Not
#BreakStmtEx7.py
word=input("Enter a Word")
result="NOT VOWEL WORD"
for ch in word:
    if(ch.lower() in ['a','e','i','o']):
         result="VOWEL WORLD"
         break
    print("\t{} is {}".format(word,result))

#Program for accepting a Name  and decide whether It is valid or not
#BreakStmtEx8.py
name=input("ENter Ur Name:")
if name.isspace():
    print("Don't enter space for Name")
else:
    words=name.split()
    result="Valid Name"
    for word in words:
        if(not word.isalpha()):
            result="InValid Name"
            break
    print("\t'{}' is {}".format(name,result)) 

#Program for Demonstrating the Need of Continue Statement
#ContinueStmtEx1.py
s="PYTHON"
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("------------------------------")
#Today:My Req:PYTON
for ch in s: #s="PYTHON" 
    if(ch=="H"):
        continue
    print(ch,end="")
else:
    print("\nelse part of loop")
print("-------------------------------")

#Program for Demonstrating the Need of Continue Statement
#ContinueStmtEx2.py
s="PYTHON"
i=0
#While(i<len(s)):
print("\t{}".format(s[i]))
i=i+1
#else:
print("else psrt of for loop")
print("------------------------------")
#Today:My Req:PYTON
i=0
while(i<len(s)): #s="PYTHON"
    if(s[i]=="H"):
        i=i+1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("\nelse part of while loop")
print("-------------------------------")    

#Program for Demonstrating the Need of Continue Statement
#ContinueStmtEx3.py
s="PYTHON"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:    
    print("else part of while loop")
print("------------------------------")
#Today:My Req:PYTON
i=0
while(i<len(s)): #s="PYTHON"
    if(s[i]=="H") or (s[i]=="Y"):
        i=i+1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("\nelse part of while loop")
    i=i+1
#else:
print("\nelse part of while loop")
print("---------------------------------")

#Program for Demonstrating the Need of Continue Statement
#ContinueStmtEx4.py
s="PYTHON"
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("------------------------------")
#Today:My Req:PYTON
for ch in s: #s="PYTHON"
    if(ch in ['H','Y']) :
        continue
    print(ch,end="")
else:
    print("\nelse part of for loop")
print("-------------------------------")

#Program for accepting a Line of Text and display all values except Vowels and space
#ContinueStmtEx5.py
line=input("ENter a Line of Text:") #python is an oop lang for ch in line:
for ch in line:
    if(ch.lower() in ['a','e','i','o','u']) or (ch.isspace()):
        continue
    print(ch,end="")

#Program for accepting Numerical Values and display separate List of +Ve and -Ve
#ListofPosNegValues.py
n=int(input("Enter How Many values u have:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list() #lst=[] --create empty list--to add the dynamic values
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=",lst) #10.0, -4.5, -20.0, 0.0, -50.0, 3.4]
        #Get +ve values
        pslist=[] #create empty list for adding +ve values 
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
        else:
            print("List of +vE Values=",pslist) 
            #Get -ve velues
            nglist=[] #create empty list for addding -ve values
            for val in lst:
                if(val>=0):
                    continue
                nglist.append(val)
            else:
                print("List of -ve values=", nglist)

#Program for accepting Numerical Values and display separate List of +Ve and -Ve
#ListofPosNegValues2.py
n=int(input("Enter How Many values u have:"))
if(n<=0):
    print("\t{} is Invalid Inpu".format(n))
else:
    lst=list() #lst=[] --creat empty list--to add the dynaic values
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=",lst) #10.0,-4.5, -20.0, 0.0, -50.0, 3.4]
        #Get +ve and -ve Values
        pslidt=[] #create empty list for adding +ve Values
        nglist=[] #creat empty list for adding -ve values
        for val in lst:
            if(val>0):
                pslidt.append(val)
            elif(val<0):
                nglist.append(val)
        else:
            print("list of +ve values=",pslist)
            print("list of -ve values=",nglist)
            nglist.extend(pslist)
            print(nglist)

#Program for Reading List of Values Dynamically and display--Most Imp
#ReadValuesEx1.py
n=int(input("Enter How Many values u want to enter:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list() #lst=[] --create empty list--to add the dynamic value
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=",lst)

#write a python program which will read number of numerical values
# and find their sum and average(mean) without using pre-defined function
#SumAvgEx1.py
n=int(input("Enter How Many value u have to find sum and avg:"))
if(n<=0):
    print("\t{} is IN=nvalid Input".format(n))
else:
    lst=list() # lst=[] --creat empty list--to add the dynamic values
    for i in range(1,n+1):
        value=float(input("Enter{} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=" ,lst) #lst=[12.0, 15.0, 20.0]
        #Find sum and avg
        s=0
        for val in lst:
            s=s+val
        else:
            print("\tsum={}".format(s))
            print("\tAvg={}".format((s/len(lst))))
            print("--------------------------------")

#write a python program which will read number of numerical values
# and find their sum and average(mean) with  pre-defined function-sum()
#SumAvgEx1.py
n=int(input("Enter How Many values u have to find sum and avg:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list() #lst=[] --create empyty list--to add the dymic values
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=",lst) #lst=[12.0, 15.0, 20.0]
        print("\tsum={}".format(sum(lst)))
        print("\Avg={}".format((sum(lst)/len(lst))))
        print("--------------------------------")

#Program for accepting a Line of Text and display all values except Vowels and space
#without using continue statement
#WithContinueStmtEx5.py
lone=input("Enter line of Text:") #Apple is in red for ch in line:
for ch in line:
    if(ch.lower() in ['a','e','i','o','u']) or (ch.isspace()):pass
    else:
        print(ch,end="")