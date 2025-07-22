#program for Demonstrating the Need of Inner OR Nested loops-for in for
#InnerLoopEx1.py
for i in range(1,5): #outer loop
    print("outer Loop of i={}".format(i))
    print("-"*50)
    for j in range(1,4): #Inner loop
        print("\t\tInner Loop of j={}".format(j))
    else:
        print("\t\telse part of inner loop")
        print("-"*50)
else:
    print("\t\telse part of outer loop")

#program for Demonstrating the Need of Inner OR Nested loops-while in while
#InnerLoopEx2.py
i=1
while(i<=3): #Inner loop
    print("\t\tInner Loop-value of j={}".format(j))
    j=j+1
    #else:
    i=j+1
    print("\t\telse part of inner loop")
    print("-"*50)
else:
    print("else part of outer loop")

#program for Demonstrating the Need of Inner OR Nested loops-for in while
#InnerLoopEx3.py
i=4
while(i>=1): #outer loop
    print("outer loop of i={}".format(i))
    print("-"*50)
    for j in range(3,0,-1): #Inner loop
        print("\t\tInner Loop-value of j={}".format(j))
    else:
        i=i-1
        print("\t\telse part of inner loop")
        print("-"*50)
else:
    print("else part of outer loop")

#program for Demonstrating the Need of Inner OR Nested loops-while in for
#InnerLoopEx4.py
for i in range(1,5): #outer loop
    print("outer Loop-value of i={}".format) 
    print("-"*50) 
    j=1
    while(j<=3): #Inner loop
        print("\t\tInner Loop-value of j={}".format(j))
        j=j+1
    else:
        print("\t\telse part of inner loop")
        print("-"*50)
else:
    print("\t\telse part of outer loop")         

#Program for generating 1 to N Mul table where N is +Ve
#InnerLoopEx5.py
n=int(input("Enter How Many Mul table u wnat to generate:")) #n=5
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    for num in range(1,n+1): #outer for loop--supply the num to inner loop
        print("-"*50)
        print("Mul Table for :{}".format(num))
        print("-"*50)
        for i in range(1,11):#Inner loop--generate Mui Table for outer loop supplied num
            print("\t{} x {}={}".format(num,i,num*1))
        else:
            print("-"*50)

#Program for generating Mul tables for Random Dynamic Values.
#InnerLoopEx6.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=list() # lst=[]--creat empty list--to add the dynamic values
    for i in range(1,n+1):
        value=int(input("Enter  {} value:".format(i)))
        lst.append(value)
    else:
        print("List of values=",lst)#[19,0,17,-4] 
        #code for generating mul tables for above list for num in lst #outer loop
        for num in lst: #outer loop
            print("-"*50)
            if(num<=0):
                print("\t{} is Invalid input".format(num))
            else:
                print("Mul Table for:{}".format(num))
                print("-"*50)
                for i in range(1,11): # Inner loop
                    print("\t\t{} x {} = {}".format(num,i,num*i)) 
                else:
                    print("-"*50)

#Program for generating List of Primes within the given range
#InnerLoopEx7.py
rangeval=int(input("Enetr Range in which u want primes:"))
if(rangeval<=1):
    print("\t{} is Invalid Input".format(rangeval))
else:
    print("-"*50)
    print("List of primes within {}".format(rangeval))
    print("-"*50)
    for num in range(2,rangeval+1): #outer loop--supply  the number
        resut=True 
        for i in range(2,num):
            if(num%i==0):
                result=False
                break
            if(result):
                print("\t\t{}".format(num))
    print("-"*50)

#Program for generating List of Primes within the given range
#InnerLoopEx8.py
rangeval=int(input("Enter Range in which u want primes:"))
if(rangeval<=1):
    print("\t{} is Invalid Input".format(rangeval))
else:
    primeslist=[] 
    for num in range(2,rangeval+1): #outer loop--supply the number  
        result=True
        for i in range(2,num):
            if(num%i==0):
                result=False
                break
            if(result):
                primeslist.append(num)
        print("-"*50)
        print("List of primes withinm{}\n".format(rangeval,primeslist)) 
        print("-"*50)
                 



