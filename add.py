s1={10,"RS",34.56,True}
print(s1,type(s1),id(s1))
s1.add("HYD")
print(s1,type(s1),id(s1))
s1.add(3.4)
print(s1,type(s1),id(s1))

s1=set()
print(s1,type(s1),id(s1))
s1.add(100)
s1.add(45.67)
s1.add(True)
s1.add("HYD")
print(s1,type(s1),id(s1))

#remove
s1={10,"RS,34.56",True}
print(s1,type(s1),id(s1))
s1.remove(10)
print(s1,type(s1),id(s1))
s1.remove(True)
print(s1,type(s1),id(s1))

#discard()
s1={10,"RS",34.56,True}
print(s1,type(s1),id(s1))
s1.discard(10)
print(s1,type(s1),id(s1))
s1.discard('RS')
print(s1,type(s1),id(s1))

#pop()
s={10,20,30,40,50,"HYD",34.56,"NL","RS"}
s.pop()
s.pop()
s.pop()
s.pop()

#clear()
s={10,20,30,40,50,"HYD",34,56,"NL","RS"}
len(s)
s.clear()
len(s)
print(s)
print(s.clear())
print(set().clear())

#copy
s1={10,"RS",34.56,'RS'}
print(s1,type(s1),id(s1))
s2=s1.copy() #shallow copy
print(s2,type(s2),id(s2))
s1.add(123)
s2.add("HYD")
print(s1,type(s1),id(s1))
print(s2,type(s2),id(s2))
s3=s1 #deep copy
print(s3,type(s3),id(s1))
s1.remove(34.56)
print(s1,type(s1),id(s3))
print(s3,type(s3),id(s3))

#isdisjoint()
s1={10,20,30,40}
s2={10,15,25,35}
s3={1,2,3,4,5}
s1.isdisjoint(s3)
set().isdisjoint (set())

#issuperset
s1={10,20,30,40}
s2={10,20}
s3={15,25,10}
s1.issuperset(s2)
s2.issuperset(s3)
s2.issuperset(s3)
s2.issuperset(s1)
set().issuperset(s1)

#issubset
s1={10,20,30}
s2={30,20,50}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.union(s2)
print(s3,type(s3))
s3={1,2,3}
s4=s1.union(s2,s3)
print(s4,type(s4))

#union()
s1={10,20,30}
s2={30,20,50}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.union(s2)
print(s3,type(s3))
s3={1,2,3}
s4=s1.union(s2,s3)
print(s4,type(s4))

#intersection
s1={10,20,30}
s2={30,20,50}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.intersection(s2)
print(s3,type(s3))
s3={10,20,30}.intersection({1,2,3})
print(s3,type(s3))
s3={10,20,30}.intersection({1,2,3},{10,4,6})
print(s3,type(s3))
s3={10}.intersection({10},{20})
print(s3,type(s3))
s3={10}.intersection({10},{10,20})
print(s3,type(s3))
set(list("RADAR")).intersection(set(list("HYD")))

#difference()
s1={10,20,30}
s2={30,40,50}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.difference(s2)
print(s3,type(s3))
s4=s2.difference(s1)
print(s4,type(s4))

#symmetric_difference()
s1={10,20,30}
s2={30,40,50}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.symmetric_difference(s2)
print(s3,type(s3))

#update
s1={10,20,30}
s2={"RS","TR"}
print(s1)
s3=s1.update(s2)
print(s3)
print(s1)

s1={10,20,30}
s2={10,20,30}
print(s1)
print(s2)
s2.update(s1)
print(s2)
print(s1)

s1={10,20,0}
s2={10,20,30}
s1.update(s2)
print(s1)

#intersection_update()
s1={10,20,30}
s2={10,20,40,50}
s3=s1.intersection_update(s2)
print(s3)
print(s1)

s1={10,20,30}
s2={10,20,40,50}
s3=s1.intersection_update(s2)
print(s1)

s1={10,20,30}
s2={1,2,3,4}
s1.intersection_update(s2)
print(s1)

#difference_update
s1={10,20,30}
s2={10,20,30}
s1.difference_update(s2)
print(s1)

s1={10,20,30}
s2={10,20,30}
s1.difference_update(s2)
print(s1)

s1={10,20,30}
s2={1,2,3}
s1.difference_update(s2)
print(s1)

#symmetric_difference_update()
s1={10,20,30}
s2={1,2,3}
s1.symmetric_difference_update(s2)
print(s1)

s1={10,20,30}
s2={10,20,3}
s1.symmetric_difference_update(s2)
print(s1)

s1={10,20,30}
s2={10,20,30}
s1.symmetric_difference_update(s2)
print(s1)

#set with set,list or nested or sets
#s1={10,"Rossum",[16,19,18],[77,76,75],"OUCET"} #TypeError:unhashable type:set

#case2
#s1={10,"Rossum",[16,19,18],[77,76,75],"OUCET"}#TypeError:unhashable type:'list'

#case3
#s1={10,"Rossum",[16,19,18],[77,76,75],"OUCET"}
print(s1,type(s1))
for val in s1:
    print(val,type(val))

#case-4
lst=[10,"Rossum",{16,19,18},{77,76,75},"OUCET"]
print(lst,type(lst))
print(lst[2],type(lst[2]))
lst[2].add(15)
print(lst)
lst[-2].add(66)
print(lst)

#case5
tpl=(10,"Rossum",{16,19,18},{77,76,75},"OUCET")
print(tpl,type(tpl))
print(tpl[2],type(tpl[2]))
tpl[2].add(15)
print(tpl,type(tpl))
tpl[-2].remove(76)
print(tpl,type(tpl))

#By using set functions
cp={"Rohit","virat","salt","Rossum"}
tp={"Rossum","Travis","Hunter","kinney"}
print(cp,type(cp))
print(tp,type(tp))
allcptp=cp.union(tp)
print(allcptp,type(allcptp))

cp={"Rohit","virat","salt","Rossum"}
tp={"Rossum","Travis","Hunter","kinney"}
print(cp,type(cp))
print(tp,type(tp))
bothcptp=cp.intersection(tp)
print(bothcptp,type(bothcptp))

cp={"Rohit","virat","salt","Rossum"}
tp={"Rossum","Travis","Hunter","kinney"}
print(cp,type(cp))
print(tp,type(tp))
onlycp=cp.difference(tp)
print(onlycp,type(onlycp))

cp={"Rohit","Virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","Kinney"}
print(cp,type(cp))
print(tp,type(tp))
onlytp=tp.difference(cp)
print(onlytp,type(onlytp))

cp={"Rohit","virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","Kinney"}
print(cp,type(cp))
print(tp,type(tp))
exclcptp=cp.symmetric_difference(tp)
print(exclcptp,type(exclcptp))

#dont use set functions,we use BITWISE operators.
cp={"Rohit","Virat","Salt","Kinney"}
tp={"Rossum","Travis","hunter","kinney"}
print(cp,type(cp))
print(tp,type(tp))
allcptp=cp|tp #bitwise or(|)
print(allcptp,type(allcptp))

cp={"Rohit","Virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","Kinney"}
print(cp,type(cp))
print(tp,type(tp))
bothcptp=cp&tp #bitwise and operator
print(bothcptp,type(bothcptp))

cp={"Rohit","Virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","kinney"}
print(cp,type(cp))
print(tp,type(tp))
onlycp=cp-tp#arithmetic minus operator (-)
print(onlycp,type(onlycp))

cp={"Rohit","Virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","Kinney"}
print(cp,type(cp))
print(tp,type(tp))
only=tp-cp#arithmetic minus operator(-)
print(onlytp,type(onlytp))

cp={"Rohit","Virat","Salt","Rossum"}
tp={"Rossum","Travis","Hunter","Kinney"}
print(cp,type(cp))
print(tp,type(tp))
exclcptp=cp^tp#bitwise xor (^)
print(exclcptp,type(exclcptp))
print(exclcptp,type(exclcptp))



