##FromImportStmtEx1.py
#from icici import bname, addr, simpleint
#from MathsInfo import PI, E
#from Aop import sumop, subop, mulop
print("--------------------------------------")
#sumop(10,20)
#mulop(10,20)
print("---------------------------------------")

#FromImportStmtEx2.py
#from icici improt bname as bn, addr as ad, simpleint as simpleint
#from MathsInfo import PI as p,E
#from AOP import sumop as ap,subop as sp ,mulop as mp
print("--------------------------------------")
#print("Bank Namme:",bn)
#print("Bank Addr:",ad)
#si()
print("-------------------------------------------")
#print(p)
#print(E)
print("-------------------------------------------")
#ap(10,20)
#sp(10,20)
#mp(10,20)
print("--------------------------------------------------")

#FromImportStmtEx1.py
#from icici import *
#from MathsInfo import *
#from Aop import *
print("------------------------------------")
#print("Bank Name:",bname)
#print("Bank Addr:",addr)
#simpleint()
print("------------------------------------")
#print(PI)
#print(E)
print("------------------------------------")
#sumop(10,20)
#subop(10,20)
#mulop(10,20)
print("------------------------------------")

#icici.py<---File Name and Module Name
bname="ICICI"
addr="AMPT-HYD" # Here bname and addr are called global Variables
def simpleint():#Function Def
    p = float(input("Enter Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    # Cal si and totamt to pay
    si = (p * t * r) / 100
    totamt = p + si
    # display the result
    print("*" * 50)
    print("\t\tPrinciple Amount:{}".format(p))
    print("\t\tTime:{}".format(t))
    print("\t\tRate of Interest:{}".format(r))
    print("\t\tSIMPLE INTEREST:{}".format(si))
    print("\t\tTOTAL AMOUNT TO PAY:{}".format(totamt))
    print("*" * 50)

#ImportStmtEx1.py
#import icici
#import MathsInfo
#import Aop
print("------------------------------------")
#print("Bank Name:",icici.bname)
#print("Bank Addr:",icici.addr)
#icici.simpleint()
print("------------------------------------")
#print(MathsInfo.PI)
#print(MathsInfo.E)
print("------------------------------------")
#Aop.sumop(10,20)
#Aop.subop(10,20)
#Aop.mulop(10,20)
print("------------------------------------")

#ImportStmtEx2.py
#import icici,MathsInfo,Aop
print("------------------------------------")
#print("Bank Name:",icici.bname)
#print("Bank Addr:",icici.addr)
#icici.simpleint()
print("------------------------------------")
#print(MathsInfo.PI)
#print(MathsInfo.E)
print("------------------------------------")
#Aop.sumop(10,20)
#Aop.subop(10,20)
#Aop.mulop(10,20)
print("------------------------------------")

#ImportStmtEx3.py
#import icici as ic
#import MathsInfo as m
#import Aop as ap
print("------------------------------------")
#print("Bank Name:",ic.bname)
#print("Bank Addr:",ic.addr)
#ic.simpleint()
print("------------------------------------")
#print(m.PI)
#print(m.E)
#print("------------------------------------")
#ap.sumop(10,20)
#ap.subop(10,20)
#ap.mulop(10,20)
print("------------------------------------")

#ImportStmtEx2.py
#import icici as ic,MathsInfo as m,Aop as ap
print("------------------------------------")
#print("Bank Name:",ic.bname)
#print("Bank Addr:",ic.addr)
#ic.simpleint()
print("------------------------------------")
#print(m.PI)
#print(m.E)
print("------------------------------------")
#ap.sumop(10,20)
#ap.subop(10,20)
#ap.mulop(10,20)
print("------------------------------------")

#MathsInfo.py<---File Name and acts as Module Name--Contains Global Variables
PI=3.173
E=2.71 # Here PI and E are called Global Variables

#SE1.py<-----File Name and It is Program
#import MathsInfo
#print(MathsInfo.PI)
#print(MathsInfo.E)

#SE2.py
#import Aop
#Aop.sumop(10,20)
#Aop.subop(10,20)
#Aop.mulop(10,20)

#SE3.py<----File Name and Program
#import icici
#print("Bank Name:",icici.bname)
#print("Bank Addr:",icici.addr)
#icici.simpleint()

