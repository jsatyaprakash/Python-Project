#program for accepting Two Values from End0-User (KBD) and cal div
# and also handle the exceptions if Possible
#DivDemo.py<---File Name and Program
#from DivOperation import division
#from DivOperation import DenZeroError
try:
    k=float(input("Enter First Value:"))
    v=float(input("Enter Second Value:"))
    #r=division(k,v) # Function Call--Gives either Result OR exception
#except DenZeroError:
    print("\tDON'T ENTER ZERO FOR DEN....")
except ValueError:
    print("\tDON'T ENTER STRS/ALNUMS/SYMBOLS")
else:
    #print("\tDiv({},{})={}".format(k,v,r))

#Phase-3: Handling the exceptions

#program for accepting Two Values from End0-User (KBD) and cal div
# and also handle the exceptions if Possible
#DivDemo2.py<---File Name and Program
#from DivOperation import division
#from DivOperation import DenZeroError
#try:
    k=float(input("Enter First Value:"))
    v=float(input("Enter Second Value:"))
    #r=division(k,v) # Function Call--Gives either Result OR exception
#except (DenZeroError,ValueError):
    print("\tDON'T ENTER ZERO FOR DEN....")
    print("\tDON'T ENTER STRS/ALNUMS/SYMBOLS")
#else:
   # print("\tDiv({},{})={}".format(k,v,r))

#Phase-3: Handling the exceptions

#DivExcept.py<-----File Name and Module Name--Step-3
        #(1)           (2)
class DenZeroError(Exception):pass


#Phase-1: Development of Programmer Exception

#program for Calculating Div of Two Numebrs and Hit OR raise  the exception
#DivOperation.py<---File Name and Module Name
#from DivExcept import DenZeroError
def division(a,b):
    if(b==0):
        raise DenZeroError # Hitting the exception
    else:
        return a/b # Gives Result

#Phase-2: Hitting OR Raising the exception.

#MulExcept.py
class ZeroError(Exception):pass
class NegativeNumError(BaseException):pass

#MulTable.py
#from MulExcept import ZeroError, NegativeNumError
def table(n):
    if(n==0):
        raise ZeroError
    elif(n<0):
        raise NegativeNumError
    else:
        print("-"*50)
        print("\tMul Table for :{}".format(n))
        print("-" * 50)
        for i in range(1,11):
            print("\t{} x {}={}".format(n,i,n*i))
        else:
            print("-" * 50)

#MulTableDemo.py
#from MulExcept import ZeroError, NegativeNumError
#from MulTable import table
try:
    n=int(input("Enter a Number for Gen Mul Table:"))
    table(n) # Fucntion Call--gives result and exceptions
except ZeroError:
    print("\tDON'T ENTER ZERO FOR MUL TABLE")
except NegativeNumError:
    print("\tDON'T ENTER -VE NUMBER FOR MUL TABLE")
except ValueError:
    print("\tDON'T ENTER ALNUMS/STRS / SUMBOLS")

