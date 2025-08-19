#program for Demonstrating Opening the File
#FileOpenEx1.py
try:
    fp=open("kvr1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("--------else block-------------")
    print("File Opened in read Mode")
    print("Type of fp=", type(fp))
    print("else block:Is File Closed?:",fp.closed)
    print("-------------------------------")
finally:
    print("I am from Finally Block")
    try:
        fp.close() # Relinquish the Resource--Manually closing
        print("finally block:Is File Closed?:", fp.closed)
    except NameError:
        print("File Name Itself does not opened-there is no need to close:")

#program for Demonstrating Opening the File
#FileOpenEx2.py
fp=open("sample.py","w")
print("File Created and Opened in Write Mode")
print("Type of fp=",type(fp))  # <class '_io.TextIOWrapper'>

#program for Demonstrating Opening the File
#FileOpenEx1.py
try:
    with open("kvr2.data","r") as fp:
        print("--------with open() as-------------")
        print("\tFile Opened in read Mode")
        print("\tType of fp=", type(fp))
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("-------------------------------------")
    print("--------afterwith open() as-------------")
    print("\tafter with open() as: Is File Closed?:", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")

#program for Demonstrating Opening the File
#FileOpenEx3.py
try:
    with open("kvr2.data","r") as fp:
        print("--------with open() as-------------")
        print("\tFile Opened in read Mode")
        print("\tType of fp=", type(fp))
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("-------------------------------------")
    print("--------afterwith open() as-------------")
    print("\tafter with open() as: Is File Closed?:", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")

#program for Demonstrating Opening the File along with File attributes
#FileOpenEx4.py
try:
    with open("kvr2.data","a+") as fp:
        print("----------------------------------------")
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("\tFile Name:{}".format(fp.name))
        print("\tFile Opening Mode:{}".format(fp.mode))
        print("\tIs File Readable? :{}".format(fp.readable()))
        print("\tIs File Writable? :{}".format(fp.writable()))
        print("-----------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#program for Demonstrating Opening the File along with File attributes
#FileOpenEx5.py
try:
    with open("kvr4.data","x+") as fp:
        print("----------------------------------------")
        print("\twith open() as: Is File Closed?:", fp.closed)
        print("\tFile Name:{}".format(fp.name))
        print("\tFile Opening Mode:{}".format(fp.mode))
        print("\tIs File Readable? :{}".format(fp.readable()))
        print("\tIs File Writable? :{}".format(fp.writable()))
        print("-----------------------------------------")
except FileExistsError:
    print("File Name alerady Exist")

#Writing the Data to the File
#Write a Python Program which will copy the content of One File into another File.
#FileCopyEx.py
def filecopy():
    try:
        srcfile=input("Enter Source File Name:")
        with open(srcfile,"r") as rp: # Opened the Source File in Read Mode
            destfile=input("Enter Destination File:")
            with open(destfile,"a") as wp: # Opened the Dest File in write Mode
                #read the Data from Source File
                srcfiledata=rp.read()
                #Write the srcfiledata to the Destination file
                wp.write(srcfiledata)
                print("Source File Data copied into Destnation file")
    except FileNotFoundError:
        print("Source File Does not Exist")
#Main Program
filecopy() # Function Call

#Program for Writing the data to the File
#FileWriteEx1.py
sno=300
sname="Kinney"
marks=63.45 # here sno,sname and marks are called Objects resides in Main Memory.
with open("student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")

#Program for Writing the data to the File
#FileWriteEx2.py
print("------------------------------------")
sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student Marks:"))
print("------------------------------------")
with open("E:\\KVR-PYTHON-7AM\\FILES\\student.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")

#Program for Writing the data to the File
#FileWriteEx3.py
x={1:"PYTHON",2:"C",3:"JAVA",4:"HTML"}
with open("itrobj.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the File")

#Reading the Data from Files
#program for Reading the Data from File.
#FileReadEx1.py
try:
    with open("E:\\KVR-PYTHON-7AM\\FILES\\student.data","r") as fp:
        filedata=fp.read()
        print("--------------------------------")
        print(filedata)
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#program for Reading the Data from File.
#FileReadEx2.py
try:
    with open("E:\\KVR-PYTHON-7AM\\FILES\\student.data","r") as fp:
        filedata=fp.readlines()
        print("--------------------------------")
        for record in filedata:
            print(record,end="")
        print("--------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#Write a Python Program which will read any file name and display Its Content.
#FileReadEx3.py
try:
    filename=input("Enter Any File Name:")
    with open(filename,"rt") as fp:
        filedata=fp.read()
        print("-------------------------------------")
        print(filedata)
        print("-------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")

#Pickling  and Un-Pickling
# (OR)
#Object Serialization or Object De-Serialization
#program for Reading Emp Values from Key Board and save them as Record in File
#By using Pickling Operation
#EmpPickEx1.py
import pickle
def saverecord():
    with open("emp.pick","ab") as fp:
        while(True):
            print("-"*50)
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("-" * 50)
            #Place the employee values in iterable Object
            lst=list() # create an empty list
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #Save the Iterable Object data into the file
            pickle.dump(lst,fp)
            print("Employee Record Saved in File Sucessfully")
            print("-" * 50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this program")
                break

#Main Program
saverecord() # Function call

#Program for read the records from file(emp.pick) by using un-pickling process.
#EmpUnPickEx1.py
import pickle
def readrecords():
    try:
        print("-"*50)
        with open("emp.pick","rb") as fp:
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-" * 50)
                    break
    except FileNotFoundError:
        print("File Does not Exist")

#Main Program
readrecords()
