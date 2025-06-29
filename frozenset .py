# s1={10,20,30,10,20,60,70}
# print(s1,type(s1))
# fs1=frozenset(11)
# print(fs1,type(fs1))
# s1={10,"RS",33.33,True}
# print(s1,type(s1))
# fs2=frozenset(s1)
# print(fs2,type(fs2))
# len(fs2)
# fs3=frozenset()
# print(fs3,type(fs3))
# len(fs3)

# s=[10,20,30,"RS",True]
# print(s,type(s))
# fs=frozenset(s)
# print(fs,type(fs))

# s1={10,"RS",33.33,True}
# print(s1,type(s1))
# fs2=frozenset(s1)
# print(fs2,type(fs2))
# fs2[0] #TypeError:'frozenset' object is not subscriptable
# fs2[0.3]  #TypeError:'frozenset' object is not subscriptable
# fs2[0]=23  #TypeError:'frozenset' object does not support item assignment

# del fs2[0]  #TypeError:'frozenset' object doesn't support item deletion
# del fs2[0:2] #TypeError:'frozenset' object doesn't support item deletion 
# del fs2 #possible
# print(fs2) #NameError:name'fs2' is not found 

# #pre-defined functions in frozenset 
# print(fs1,type(fs1),id(fs1))
# fa2=fs1.copy()
# print(fs1)

# fs1=frozenset({10,20,30,40,50,60,70})
# fs2=frozenset((10,20,30))
# fs1.issuperset(fs2)
# fs2.issuperset(fs1)
# fs2.issuperset(fs1)
# fs1.issuperset(fs2)

# fs1=frozenset({10,20,30,40,50,60,70})
# fs2=frozenset((100,200,300))
# fs3=frozenset((10,2,3))
# fs1.isdisjoint(fs2)
# fs1.isdisjoint(fs3)
# print(fs1)
# print(fs2)
# fs1.union(fs2)
# fs1.intersection(fs2)
# fs1.difference(fs1)
# fs2.difference

# #dict category data type
# d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
# print(d1,type(d1))
# len(d1)
# d2={"Python":1,"C":2,"Java":3,"C++":4}
# print(d2,type(d2))
# len(d2)

# d1={10:1.2,10:2.3,10:4.5,10:0.2}
# print(d1)
# d1={10:1.2,20:2.3,10:1.9,80:2.9}
# print(d1)

# d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
# print(d1,type(d1))
# d1[0]
# d1[10]
# d1[20]
# d1[30]
# d1[40]
# d1[50]#keyError:50

# d1={10:"Apple",20:"Mango",30:"Kiwi",40:"sberry"}
# print(d1,type(d1),id(d1))
# d1[10]="Guava"#udating value of value by using value of key
# print(d1,type(d1),id(d1))

# d1={}
# print(d1,type(d1))
# len(d1)

# d2=dict()
# print(d2,type(d2))
# len(d2)

# d1={}
# print(d1,type(d1),id(d1))
# len(d1)
# d1[100]=1.2 #Inserted Entry
# d1[200]=2.2 #Inserted Entry
# d1[300]=1.2 #Inserted Entry
# d1[400]=4.2 #Inserted Entry
# print(d1,type(d1),id(d1))
# len(d1)
# d1[500]=5.5 #Inserted Entry
# print(d1,type(d1),id(d1))
# d1[300]=0.2 #Modified Entry bcoz the key 300 already exist in d1
# print(d1,type(d1),id(d1))

#pre-defined functions in dict
#clear()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
len(d1)
d1.clear()
print(d1,type(d1),id(d1))
len(d1)
print(d1.clear())
print({}.clear())
print(dict().clear())

#pop()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d1.pop(20)
print(d1,type(d1),id(d1))
d1=(30)
print(d1,type(d1),id(d1))
#d1.pop(40)
#print(d1,type(d1),id(d1))
#d1.pop(30) #keyError:30
#{}.pop(10) #keyError:30
#dict().pop(20) #keyError:30

#popitem()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
#print(d1,type(d1,id(d1)))
#d1.popitem() #keyError:'popitem():dictionary is empty'
#{}.popitem() #keyError:'popitem():dictionary is empty'
#dict().popitem() #keyError:'popitem():dictionary is empty'

#copy()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d2=d1.copy() #shallow copy
print(d1,type(d2),id(d2))
#d1[10]=12.3
#d2=[40]=14.4 
#print(d1,type(d1,id(d1)))
#print(d2,type(d2),id(d2))

#get   Most Imp
d1={10:1.2,2.:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
val=d1.get(10)
print(val)
val=d1.get(20)
print(val)
val=d1.get(200)
print(val)
statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG",}
print(statescaps)
cap=statescaps.get("TS")
print(cap)
cap=statescaps.get("KAR")
print(cap)
cap=statescaps.get("AMPT")
print(cap)
print({}.get(10))

d1={10:1.2,20:2.2,30:2.2,40:4.4}
d1[10]
d1[40]
#d1[400]#keyError:400

#key()
#statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
#print(statescaps)
#states=statescaps.key()
#print(states,type(states))
#for k in states:
   # print(k)
#for k in statescaps.keys():
    #print(k)
#for k in {10:"Apple",20:"Mango",30:"Kiwi"}.key():
    #print(k,"-->",{10:"Apple",20:"Mango",30:"Kiwi"}[k])
#for k in {10:"Apple",20:"Mango",30:"Kiwi"}.key():
        #print(k,"-->",{10:"Apple",20:"Mango",30:"Kiwi"}.get(k))
#for de in enumerate(statescaps):
     #print(de)
#for de in enumerate(statescaps):
     #print(de,"-->",statescaps[de[1]])     
#for de in enumerate(statescaps):
     #print(de,"-->",statescaps.get(de[1]))

#values()
statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)
#caps=statescaps.value()
     #print(cap,type(caps))
#for v in caps:
     #print(v)
#for v in statescaps.values():
     #print(v)
#for v in {'ts':'HYD','AP':'VIJ',"KAR":'BANG','MH':'MUM'}.values():
     #print(v)

#item()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1)
#kvs=d1.item()
    #print(kvs,type(kvs))
#for kv in kvs:
    # print(kv)
#for kv in kvs:
     #print(kv[0],"-->",kv[1])
#for kv in d1.item():
     #print(kv[0],"-->",kv[1])
#for k,v in d1.item():
    # print(k,"==>",v)
d1={10:1.2,20:2.2,30:3.4,40:1.2}
print(d1)
for x in d1:
    print(x)
for x in d1:
    print(x,"-->",d1[x])
for x in d1:
    print(x,"-->",d1.get(x))

#update()
d1={10:1.2,20:2.3}
d2={30:3.3,40:4.4}
d1.update(d2)
print(d1)

d1={10:1.2,20:2.3}
d2={20:13.3,40:4.4}
d2.update(d1)
print(d2)

d1={10:11.2,20:12.3}
d2={10:1.2,20:2.3}
d1.update(d2)
print(d1)


