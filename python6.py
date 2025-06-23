a=12.34
print(a,type(a))
b=(a)
print(b,type(b))
b=int(0.12)
print(b,type(b))

a=True
print(a,type(a))
b=int(a)
print(b,type(b))
b=False
print(b,type(b))

a=2+3j
print(a,type(a))

b=int(a.real)
print(b,type(b))
b=int(a.imag)
print(b,type(b))

a="12"
print(a,type(a))
b=int(a)
print(b,type(b))

a="12.34"
print(a,type(a))

a="True"
print(a,type(a))

"2+3.5j"
print(a,type(a))

a="PYTHON"
print(a,type(a))

a="2xyz"
print(a,type(a))

a="2xyz"
print(a,type(a))
a[0]
b=int(a[0])
print(b,type(b))


#float
a=12
print(a,type(a))
b=float(a)
print(b,type(b))
b=float(0)
print(b,type(b))

a=True
print(a,type(a))
b=float(a)
print(b,type(b))
b=float(False)
print(b,type(b))

a=2+3.5j
print(a,type(a))

a="123"
print(a,type(a))
b=float(a)
print(b,type(b))
b=float("12")
print(b,type(b))

a="12.34"
print(a,type(a))
b=float(a)
print(b,type(b))

a="True"
print(a,type(a))

a="2+3.5j"


#list
lst=[10,20,30,12.34,10,20,-45,67]
print(lst,type(lst))
lst2=[100,"Rossum",45.67,2+3j,True]
print(lst2,type(lst2))

lst2=[100,"Rossum",45,67,2+3j,True]
print(lst2,type(lst2))
lst2[0]
lst2[-5]
lst2[-1]
lst[1]
lst2[1:3]
["Rossum",45.67]

lst2[0]=5555    #index based upadation
print(lst2,type(lst)) 
lst2[1:3]=["Guido",99.88]    #slice based upadition
print(lst2,type(lst2))

lst1=[]
print(lst1,type(lst1))
lst2=[]
print(lst2,type(lst2))

s="MISSISSIPPI"
print(s,type(s))
lst1=list(s)
print(lst1,type(lst1))

a=10
print(a,type(a))
lst1=list([a])
print(lst1,type(list))

#append()
lst=[10,"RS",34.56]
print(lst,type(lst),id(lst))
lst.append("NL")
print(lst,type(lst),id(lst))
lst.append(True)
print(lst,type(lst),id(lst))

lst1=[]
print(lst1,type(lst1),id(lst1))
lst1.append(100)
lst1.append("DR")
lst1.append(True)
print(lst1,type(lst1),id(lst1))

#insert()
lst=[10,"45.67","PYTHON"]
lst.insert(2,"NL")
print(lst,type(lst),id(lst))
lst.insert(0,100)
print(lst,type(lst),id(lst))
lst.insert(-1,"HYD")
print(lst,type(lst),id(lst))

#remove()
lst=[10,"RS",45.67,"PYTHON",2+3j]
print(lst,type(lst),id(lst))
lst.remove("PYTHON")
print(lst,type(lst),id(lst))

lst=[10,20,30,10,20,40,50,10,20]
print(lst,type(lst),id(lst))
lst.remove(10)
print(lst,type(lst),id(lst))
lst.remove(10)
print(lst,type(lst),id(lst))

#pop(index)
lst=[10,20,30,10,20,40,50,10,20]
print(lst,type(lst),id(lst))
lst.pop(3)
print(lst,type(lst),id(lst))
lst.pop(-1)
print(lst,type(lst),id(lst))

#pop()
lst=[10,20,30,10,20,40]
print(lst,type(lst),id(lst))
lst.pop()
print(lst,type(lst),id(lst))
lst.pop()
print(lst,type(lst),id(lst))
lst.pop()
print(lst,type(lst),id(lst))
lst.pop()

#clear()
lst=[10,20,30,10,20,40]
print(lst,type(lst),id(lst))
len(lst)
lst.clear()
print(lst,type(lst),id(lst))
len(lst)

#del operator
lst=[10,20,30,10,20,40]
print(lst,id(lst))
del lst[0:3]
print(lst,id(lst))
del lst[0]
print(lst,id(lst))

#index()
lst=[100,200,300,100,400,500,200,100]
print(lst,type(lst))

#enumerate()
lst=[100,200,300,100,400,500,200,100]
print(lst)
for x in enumerate(lst):
    print(x)

    for index, value in enumerate(lst):
        print(index,"-->",value)

        for index, value in enumerate(lst):
            if (value == 200):
                print(index, "-->",value)
                1
                6
                s="PYTHON"
                for ind, val in enumerate(s):
                    print(ind, "-->", val)

                    for ind, val in enumerate(s):
                        if(val=="I"):
                            print(ind,"-->",val)
                            
                        
                            
                            
                            for ind, val in enumerate(s):
                                if(val=="s"):
                                    print(ind,"-->",val)
                                    
                                    for ind, val in enumerate(range(100,111,2)):
                                        print(ind,"-->",val)

                                        #copy()
                                        lst1=[10,"RS",34.56]
                                        print(lst1,type(lst1),id(lst1))
                                        lst2=lst1.copy() #shallow copy
                                        print(lst2,type(lst2),id(lst2))
                                        lst1.append("NL")
                                        lst2.append(1,"GUIDO")
                                        print(lst1,type(lst1),id(lst1))
                                        print(lst2,type(lst2),id(lst2))

                                         #deep copy
                                        lst1=[10,"RS",34.56]
                                        print(lst1,type(lst1),id(lst1))
                                        lst2=lst1 #deep copy
                                        print(lst2,id(lst2))
                                        lst1.append("NL")
                                        print(lst1,id(lst1))
                                        print(lst2,id(lst2))
                                        lst2.insert(1,"GD")
                                        print(lst1,id(lst1))
                                        print(lst2,id(lst2))

                                        #reverse()
                                        lst=[10,"RS",34.56]
                                        print(lst1,id(lst1))
                                        lst2=lst2.reverse()
                                        print(lst2)
                                        print(lst1,id(lst1))

                                        lst1=[10,20,15,2,3,17]
                                        print(lst1,id(lst1))
                                        lst1.reverse()
                                        print(lst1,id(lst1))

                                        lst=[10,"RS",34.56]
                                        print(lst1,id(lst1))
                                        lst2=lst1[::1]
                                        print(lst1,id(lst))
                                        print(lst2,id(lst))

                                        #sort()
                                        lst=[10,2,4,15,6,-1,0,16]
                                        print(lst,id(lst))
                                        lst.sort()
                                        print(lst,id(lst))
                                        lst.reverse()
                                        print(lst,id(lst))

                                        lst=[10,2,4,15,6,-1,0,16]
                                        print(lst,id(lst))
                                        lst.sort(reverse=True)
                                        print(lst,id(lst))
                                        lst=["Rossum","Trump","Travis","Dennis","Ritche"]
                                        print(lst)
                                        lst.sort()
                                        print(lst)
                                        lst=["Rossum","Trump","Travis","Dennis","Ritche"]
                                        print(lst)
                                        lst.sort(reverse=True)
                                        print(lst)

                                        lst=[10,"RS",34.56,2+3j]
                                        print(lst)

                                        #extend()
                                        lst=[10,20,30]
                                        lst2=["RS","TR"]
                                        print(lst1)
                                        print(lst2)
                                        lst1.extend(lst2)
                                        print(lst1)
                                        print(lst2)

                                        lst1[10,20,30]
                                        lst2=["RS","TR"]
                                        print.extend(lst)
                                        print(lst2)

                                        #alternative solution is here by using + operator
                                        lst1=[10,20,30]
                                        lst2=["RS","TR"]
                                        lst3=[1.2,3.4,5.6]
                                        print(lst1,id(lst1))
                                        lst1=lst1+lst2+lst3
                                        print(lst1,id(lst))

                                        #count()
                                        lst.count(10)
                                        lst.count(30)
                                        lst.count(300)

                                        s="MISSISSIPPI"
                                        lst=list(s)
                                        print(lst)
                                        lst.count("I")
                                        lst.count("s")

                                        #Inner list or nested list
                                        lst=[10,'Rossum', [30,35,25], [70,65,60], 'JNTU' ]
                                        print(lst,type(lst))
                                        for val in lst:
                                            print(val,"-->",type(val),"-->",type(lst))
                                            print(lst,type(lst))
                                            lst[2].append(38)
                                            print(lst)
                                            lst[-2].insert(1,58)
                                            print(lst,type(lst))
                                            lst[-2] [::3] [70,60]

                                            lst[2]+lst[3]
                                            print(lst)
                                            lst.insert(-1,lst[2]+lst[3])
                                            print(lst,type(lst))
                                            print(lst)
                                            # lst[-2][1]=lst[-2][1]+lst[-2][1]*(50/100)
                                            print(lst)
                                            lst[-2][-2:][58,60]
                                            print(lst)
                                            lst[-2].clear()
                                            print(lst)
                                            del lst[-2]
                                            print(lst)
                                            lst[-2].opp()
                                            print(lst)
                                            del lst[2:4]
                                            print(lst)
                                            lst.insert(-1,[10,30,50])
                                            print(lst)

                                            lst=[100,"RS",[18,19,17],[67,80,76],"JNTU"]
                                            print(lst,type(lst))
                                            for val in lst:
                                                print(val,"-->",type(val),"-->",type(lst))

                                                lst[2]
                                                lst[-3]
                                                lst[3]
                                                lst[-2]
                                                lst[2][1]
                                                lst[2][-2]
                                                lst[-3][1]
                                                lst[-3][-2]
                                                print(lst)
                                                lst[2].append(15)
                                                print(lst)
                                                lst[-2].insert(1,12)
                                                print(lst)
                                                lst[-3].sort()
                                                print(lst)
                                                lst[-2].sort(reverse=True)
                                                print(lst)
                                                lst.append([1.2,2.3,4.5])
                                                print(lst)
                                                lst[-1].clear()
                                                print(lst)
                                                del lst[-1]
                                                print(lst)

                                                lst.remove([15,17,18,19])
                                                print(lst)
                                                del lst[2][1:3]
                                                print(lst)
                                                lst[2].append(69)
                                                print(lst)

                                                del lst[1::2]
                                                print(lst)
                                                lst.clear()
                                                print(lst)
                                                lst.insert(0,[])
                                                print(lst)
                                                lst[0].append([])
                                                print(lst)
                                                len(lst)
                                                len(lst[0][0])

                                                lst=[[10,20,30],[40,50,60],[70,80,90]]
                                                print(lst)
                                                for val in list:
                                                    print(val)
                                                    lst=[ [ [10,20,30], [40,50,60], [70,80,90],[1,2,3],[4,5,6],[7,8,9] ] ]
                                                    print(lst)
                                                    for matrix in lst:
                                                        print(matrix)
                                                        for matrix in lst:
                                                            for row in matrix:
                                                                print(row)
                                                                print("-----------")

                                                                #tuple
                                                                t1=(10,20,30,24,10,20)
                                                                print(t1,type(t1))
                                                                t2=(100,"RS",34.56,True,2+3j)
                                                                print(t2,type(t2))

                                                                t2=(100,"RS",34.56,True,2+3j)
                                                                print(t2,type(t2))
                                                                t2[1]
                                                                t2[2]
                                                                t2[0:3]
                                                                t2[::-1]
                                                                t2[::2]

                                                                t2=(100,"RS",34.56,True,2+3j)
                                                                print(t2,type(t2))
                                                                t2[0]

                                                                t1=()
                                                                print(t1,type(t1))
                                                                len(t1)
                                                                t2=tuple()
                                                                print(t2,type(t2))
                                                                len(t2)

                                                                t2=(100,"RS",34.56,True,2+3j)
                                                                print(t2,type(t2))
                                                                len(t2)
                                                                t3=10,"Travis",45.67,"HYD"
                                                                print(t3,type(3))

                                                                s="PYTHON"
                                                                print(s,type(s))
                                                                t=tuple(s)
                                                                print(t,type(t))
                                                                 
                                                                s="PYTHON"
                                                                print(s,type(s))
                                                                t=tuple([s])
                                                                print(t,type(t))
                                                                x=10
                                                                print(x,type(x))
                                                                x=10
                                                                print(x,type(x))

                                                                a=10
                                                                print(a,type(a))
                                                                t=tuple([a])
                                                                print(t,type(t))
                                                                t1=tuple((a))
                                                                print(t1,type(t1))

                                                                #pre-defined function in tuple
                                                                t1=(10,"RS",45.67)
print(t1,type(t1))
t1.index(10)
t1.index("RS")
t1=(10,"RS",45.67)
print(t1,type(t1))
t1.count(10)
t1.count(100)
t1(10,0,10,10,20,0,10)
print(t1,type(t1))
t1.count(10)
t1.count(0)
t1.count(100)

t1=(10,20,30,40,50,10)
print(t1,id(t1),type(t1))
t2=t1 #deep copy possible but not shallow copy
print(t2,id(t2),type(t2))
t3=t1 #deep copy possible but not shallow copy
print(t3,id(t3),type(t3))

t1=(10,-34,0,10,23,56,76,21)
print(t1,type(t1))

t1=(10,23,-56,-1,13,15,6,-2)
print(t1,type(t1))
x=sorted(t1)
print(x,type(x))
t1=tuple(x)#converted sorted list into tuple
print(t1,type(t1))
t2=t1[::-1]
print(t2,type(t2))

t1=(10,2,13,4,-5,23,56,5)
print(t1)
x=tuple(sorted(t1))
print(x,type(x))
print(t1)
y=tuple(sorted(t1)[::-1])
print(y,type(y))

y=tuple(sorted(t1,reverse=True))
print(y,type(y))

t1=(10,-4,12,34,16,-6,0,15)
print(t1,type(t1))
11=list(t1)
print(11,type(11))

#Nested or tuple
t1=(10,"Rossum",(17,16,18),(77,78,66),"OUCET") #Tuple in Tuple
print(t1,type(t1))
t1[0]
t2[1]
t1[2]
t1[3]
t1[2][1]
t1[-2][-1]

#list in Tuple
t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
print(t1,type(t1))
print(t1[2],type(t1[2]))
print(t1[3],type(t1[3]))
t1[2].sort()
print(t1,type(t1))
t1[3].sort(reverse=True)
print(t1,type(t1))

#tuple in list
11=[10,"Rossum",(17,16,18),(77,78,66),"OUCET"]
print(11,type(11))
11[1]
print(11[2],type(11[2]))
print(11[3],type(11[3]))

#set
s1={10,20,30,40,10,20,30,60,-45,67}
print(s1,type(s1))
s2={"Travis",45,56.78,True,2+3j}
print(s2,type(s1))
s1={10,20,30,40,10,20,30,60,-45,67}
print(s1,type(s1))
s2={"Travis",45,56.78,True,2+3j}
print(s2,type(s1))

s1={10,20,30,40,10,20,30,60,-45,67}
print(s1,type(s1))
s1.add(100)
print(s1,type(s1)),id(s1)

x=set()
print(x,type(x))
len(x)
s1={10,"RS",45.67,True}
print(s1,type(s1))

s="MISSISSIPPI"
print(s)
MISSISSIPPI
s1=set(s1)
s1=set(s)
print(s1,type(s1))
lst=[10,20,30,10,20,30,40,50,60,40]
print(lst,type(lst))
s1=set(lst)
print(s1,type(s1))

a=10
print(a,type(a))

