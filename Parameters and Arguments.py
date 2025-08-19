#Program for Demionstrating the Concept of Possitional Arguments--Used for Passing Specific Data
#PossArgsEx1.py
def dispstudvals(sno,sname,smarks):#function definition
    print("\t{}\t{}\t{}".format(sno,sname,smarks))
    #main program 
    print("-"*50)
    print("\tsno\tname\tmarks")
    print("-"*50)
    dispstudvals(100,'Rs',45.67)#function call
    dispstudvals(200,'TR',65.17)#function call
    dispstudvals(300,'DR',25.47) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(marks=34.56,sno=500,sname="MC") # Function Call with Keyword args
print("-"*50)

#Program for Demionstrating the Concept of Possitional Arguments--Used for Passing Specific Data
#PossArgsEx2.py
def dispstudvals(sno,sname,marks,crs): # Function definition
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudvals(100,'RS',45.67,"PYTHON") # Function Call
dispstudvals(200,'TR',65.17,"PYTHON") # Function Call
dispstudvals(300,'DR',25.47,"PYTHON") # Function Call
dispstudvals(400,'SS',75.17,"PYTHON") # Function Call
dispstudvals(400,'SS',75.17,"PYTHON") # Function Call
print("-"*50)

#Program for Demonstrating the Concept of Deafult Arguments--Used for  Specificying Common Data
#DefaultArgsEx1.py
def dispstudvals(sno,sname,marks,crs="PYTHON"): # Function definition
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudvals(100,'RS',45.67) # Function Call
dispstudvals(200,'TR',65.17) # Function Call
dispstudvals(300,'DR',25.47) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
print("-"*50)

#Program for Demonstrating the Concept of Deafult Arguments--Used for  Specificying Common Data
#DefaultArgsEx2.py
def dispstudvals(sno,sname,marks,crs="PYTHON"): # Function definition
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudvals(100,'RS',45.67) # Function Call
dispstudvals(200,'TR',65.17) # Function Call
dispstudvals(300,'DR',25.47) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(500,'MC',75.17,"JAVA") # Function Call
dispstudvals(600,'DT',15.17) # Function Call
print("-"*50)

#Program for Demonstrating the Concept of Deafult Arguments--Used for  Specificying Common Data
#DefaultArgsEx3.py
def dispstudvals(sno,sname,marks,crs="PYTHON",cnt="INDIA"): # Function definition
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#Main Program
print("-"*60)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("-"*60)
dispstudvals(100,'RS',45.67) # Function Call
dispstudvals(200,'TR',65.17) # Function Call
dispstudvals(300,'DR',25.47) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(400,'SS',75.17) # Function Call
dispstudvals(500,'MC',75.17,"JAVA") # Function Call
dispstudvals(600,'DT',15.17,cnt="USA") # Function Call
#dispstudvals(cnt="RSA",700,'PT',55.17,crs="HTML") # SyntaxError: positional argument follows keyword argument
dispstudvals(700,'PT',55.17,cnt="RSA",crs="HTML")
print("-"*60)

#Program for Demonstrating the concept of Keyword args
#KeywordArgsEx1.py
def  disp(a,b,c,d): # Function Def
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#main Program
print("-"*50)
print("\tA\tB\tC\tD")
print("-"*50)
disp(10,20,30,40) # Function Call with Pos Args
disp(d=40,a=10,b=20,c=30)  # Function Call with Keyword Args
disp(d=40,c=30,b=20,a=10)  # Function Call with Keyword Args
disp(10,20,d=40,c=30)# Function Call with Pos Args and Keyword Args
#disp(d=40,c=30,10,20)# SyntaxError: positional argument follows keyword argument
print("-"*50)

#Program for Demonstrating the concept of Keyword args
#KeywordArgsEx2.py
def  disp(a,b,c,d,E=2.71): # Function Def
	print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,E))

#main Program
print("-"*50)
print("\tA\tB\tC\tD\tE")
print("-"*50)
disp(10,20,30,40) # Function Call with Pos Args
disp(d=40,a=10,b=20,c=30)  # Function Call with Keyword Args
disp(d=40,c=30,b=20,a=10)  # Function Call with Keyword Args
disp(10,20,d=40,c=30)# Function Call with Pos Args and Keyword Args
disp(E=2.77,d=40,b=20,a=10,c=30) # Function Call with Keyword Args
print("-"*50)

#Program for showing the need of Variable Length Args
#This Program will not execute as It is bcoz PVM performs Interpretation Process and It remembers Latest Function Definition and more Over It contains Same Function Name
#VarlengthArgsEx1.py
def  disp(a,b,c,d): # Function Def-1 with 4 Pos Params
	print(a,b,c,d)

def  disp(a,b,c): # Function Def-2 with 3 Pos Params
	print(a,b,c)

def  disp(a,b): # Function Def-3 with 2 Pos Params
	print(a,b)

def  disp(a): # Function Def-4 with 1 Pos Param
	print(a)

#Main Program
disp(10,20,30,40) # Function Call-1 with 4 Pos. Args
disp(10,20,30) # Function Call-2 with 3 Pos. Args
disp(10,20) # Function Call-3 with 2 Pos. Args
disp(10) # Function Call-4 with 1 Pos. Args

#Program for showing the need of Variable Length Args
#This Program will  execute as It is (Limitation: If i Have 1000 Function Calls then we must define 1000 Fun Def--Takes more development time)
#VarlengthArgsEx2.py
def  disp(a,b,c,d): # Function Def-1 with 4 Pos Params
	print(a,b,c,d)

disp(10,20,30,40) # Function Call-1 with 4 Pos. Args
#-------------------------------------------------------------------------------------
def  disp(a,b,c): # Function Def-2 with 3 Pos Params
	print(a,b,c)

disp(10,20,30) # Function Call-2 with 3 Pos. Args
#-------------------------------------------------------------------------------------
def  disp(a,b): # Function Def-3 with 2 Pos Params
	print(a,b)

disp(10,20) # Function Call-3 with 2 Pos. Args
#-------------------------------------------------------------------------------------
def  disp(a): # Function Def-4 with 1 Pos Param
	print(a)
disp(10) # Function Call-4 with 1 Pos. Args

#Program for showing the need of Variable Length Args
#This Program will not execute as It is ( Advantage: Irrespective Number of Function Calls, we define single function def by the concept of Variable length args)
#PureVarlengthArgsEx1.py
def   disp( *kvr): # Here *kvr is called Variable Length Parameter and whose type is <class, tuple>
	print(kvr,type(kvr))



#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Pos. Args
disp(10,20,30,40) # Function Call-2 with 4 Pos. Args
disp(10,20,30) # Function Call-3 with 3 Pos. Args
disp(10,20) # Function Call-4 with 2 Pos. Args
disp(10) # Function Call-5 with 1 Pos. Args"""

#Program for showing the need of Variable Length Args
#This Program will not execute as It is ( Advantage: Irrespective Number of Function Calls, we define single function def by the concept of Variable length args)
#PureVarlengthArgsEx2.py
def   disp( *kvr): # Here *kvr is called Variable Length Parameter and whose type is <class, tuple>
	print("Number of Values=",len(kvr))
	for val in kvr:
		print("\t{}".format(val))
	print("-----------------------------")

#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Pos. Args
disp(10,20,30,40) # Function Call-2 with 4 Pos. Args
disp(10,20,30) # Function Call-3 with 3 Pos. Args
disp(10,20) # Function Call-4 with 2 Pos. Args
disp(10) # Function Call-5 with 1 Pos. Args
disp() # Function Call-5 with 0 Pos. Args

#Program for showing the need of Variable Length Args
#This Program will not execute as It is ( Advantage: Irrespective Number of Function Calls, we define single function def by the concept of Variable length args)
#PureVarlengthArgsEx3.py
def   disp(sno,sname,*kvr): # Here *kvr is called Variable Length Parameter and whose type is <class, tuple>
	print("Student Number:",sno)
	print("Student Name:",sname)
	print("Number of Values=",len(kvr))
	s=0
	for val in kvr:
		print("\t{}".format(val))
		s=s+val
	print("-----------------------------")
	print("Sum=",s)
	print("-----------------------------")

#Main Program
disp(100,"RS",10,20,30,40,50) # Function Call-1 with 5 Pos. Args
disp(200,"TR",10,20,30,40) # Function Call-2 with 4 Pos. Args
disp(300,"DR",10,20,30) # Function Call-3 with 3 Pos. Args
disp(400,"SR",10,20) # Function Call-4 with 2 Pos. Args
disp(500,"MC",10) # Function Call-5 with 1 Pos. Args
disp(600,"KN") # Function Call-5 with 0 Pos. Args

#Program for showing the need of Variable Length Args
#This Program will not execute as It is ( Advantage: Irrespective Number of Function Calls, we define single function def by the concept of Variable length args)
#PureVarlengthArgsEx4.py
def   disp(sno,sname,*kvr,city="HYD"): # Here *kvr is called Variable Length Parameter and whose type is <class, tuple>
	print("Student Number:",sno)
	print("Student Name:",sname)
	print("Student Living City:",city)
	print("Number of Values=",len(kvr))
	s=0
	for val in kvr:
		print("\t{}".format(val))
		s=s+val
	print("-----------------------------")
	print("Sum=",s)
	print("-----------------------------")

#Main Program
disp(100,"RS",10,20,30,40,50) # Function Call-1 with 5 Pos. Args
disp(200,"TR",10,20,30,40) # Function Call-2 with 4 Pos. Args
disp(300,"DR",10,20,30) # Function Call-3 with 3 Pos. Args
disp(400,"SR",10,20) # Function Call-4 with 2 Pos. Args
disp(500,"MC",10) # Function Call-5 with 1 Pos. Args
disp(600,"KN") # Function Call-5 with 0 Pos. Args
disp(700,"DT",1.2,2.3,4.5,city="USA")
disp(800,"PT",city="RSA")
#disp(700,"DT",city="USA",1.2,2.3,4.5)-----SyntaxError: positional argument follows keyword argument

#Program for Demonstrating the Need of Keyword Variable Length args
#This Program will not execute as It is bcoz PVM performs Interpretation Process and It remembers Latest Function Definition and more Over It contains Same Function Name
#KeywordVarLengthArgsEx1.py
def disp(eno,ename,sal,cname): # Function Def-1
	print(eno,ename,sal,cname)
def disp(tno,tname,sub1,sub2,sub3) : # Function Def-2
	print(tno,tname,sub1,sub2,sub3)
def disp(sno,sname,hb1,hb2,hb3,hb4) : # Function Def-3
	print(sno,sname,hb1,hb2,hb3,hb4)


#Main Program
disp(eno=10,ename="RS",sal=4.5,cname="PSF") # Function Call-1- with 4 Keyword args
disp(tno=100,tname='TR',sub1="Python",sub2="DSA",sub3="Django")  # Function Call-2- with 5 Keyword args
disp(sno=200,sname='DR',hb1="Chatting",hb2="Eating",hb3="Sleeping",hb4="Not Reading") # Function Call-2- with6 Keyword args

#Program for Demonstrating the Need of Keyword Variable Length args
#This Program will  execute as It is (Limitation: If i Have 1000 Function Calls then we must define 1000 Fun Def--Takes more development time)
#KeywordVarLengthArgsEx2.py
def disp(eno,ename,sal,cname): # Function Def-1
	print(eno,ename,sal,cname)
disp(eno=10,ename="RS",sal=4.5,cname="PSF") # Function Call-1- with 4 Keyword args
#----------------------------------------------------------------------------------------
def disp(tno,tname,sub1,sub2,sub3) : # Function Def-2
	print(tno,tname,sub1,sub2,sub3)
disp(tno=100,tname='TR',sub1="Python",sub2="DSA",sub3="Django")  # Function Call-2- with 5 Keyword args
#----------------------------------------------------------------------------------------
def disp(sno,sname,hb1,hb2,hb3,hb4) : # Function Def-3
	print(sno,sname,hb1,hb2,hb3,hb4)
disp(sno=200,sname='DR',hb1="Chatting",hb2="Eating",hb3="Sleeping",hb4="Not Reading") # Function Call-2- with 6 Keyword args
#----------------------------------------------------------

#Program for Demonstrating the Need of Keyword Variable Length args
#This Program will  execute as It is 
#PureKeywordVarLengthArgsEx1.py
def  disp( **kvr): # here **kvr is calle Keyword variable length args and whose type is <class, dict>
	print(kvr,type(kvr))

#Main Program
disp(eno=10,ename="RS",sal=4.5,cname="PSF") # Function Call-1- with 4 Keyword args
disp(tno=100,tname='TR',sub1="Python",sub2="DSA",sub3="Django")  # Function Call-2- with 5 Keyword args
disp(sno=200,sname='DR',hb1="Chatting",hb2="Eating",hb3="Sleeping",hb4="Not Reading") # Function Call-2- with6 Keyword args
disp(cid=1000,cname="Sai")

#Program for Demonstrating the Need of Keyword Variable Length args
#This Program will  execute as It is 
#PureKeywordVarLengthArgsEx2.py
def  disp( **kvr): # here **kvr is calle Keyword variable length args and whose type is <class, dict>
	for k,v in kvr.items():
		print("\t{}-->{}".format(k,v))
	print("---------------------------------------------------")

#Main Program
disp(eno=10,ename="RS",sal=4.5,cname="PSF") # Function Call-1- with 4 Keyword args
disp(tno=100,tname='TR',sub1="Python",sub2="DSA",sub3="Django")  # Function Call-2- with 5 Keyword args
disp(sno=200,sname='DR',hb1="Chatting",hb2="Eating",hb3="Sleeping",hb4="Not Reading") # Function Call-2- with6 Keyword args
disp(cid=1000,cname="Sai")

#PureKeywordVarLengthArgsEx3.py
def  FindTotalMarks(sno,sname,cls,**submarks):
	print("-"*50)
	print("Student Number={}".format(sno))
	print("Student Name={}".format(sname))
	print("Student Class={}".format(cls))
	print("-"*50)
	if(len(submarks)!=0):
		totmarks=0
		for subject,marks in submarks.items():
			print("\t{}----->{}".format(subject,marks))
			totmarks=totmarks+marks
		print("-"*50)
		print("TOTAL MARKS={}".format(totmarks))
	print("*"*50)

#Main program
FindTotalMarks(100,"Rossum","X",English=80,Hindi=78,Telugu=65,Maths=90,Physics=60,Chemistry=58)
FindTotalMarks(200,"Travis","XII",Eng=80,Sanskrit=78,Math_1A=75,Phy=60,Che=58)
FindTotalMarks(300,"dennis","B.Tech(CSE)",OS=50,DBMS=51,NW=34)
FindTotalMarks(400,"Kinney","Research")

#PureKeywordVarLengthArgsEx4.py
def  FindTotalMarks(sno,sname,cls,cnt="INDIA",**submarks):
	print("-"*50)
	print("Student Number={}".format(sno))
	print("Student Name={}".format(sname))
	print("Student Class={}".format(cls))
	print("Student Living City={}".format(cnt))
	print("-"*50)
	if(len(submarks)!=0):
		totmarks=0
		for subject,marks in submarks.items():
			print("\t{}----->{}".format(subject,marks))
			totmarks=totmarks+marks
		print("-"*50)
		print("TOTAL MARKS={}".format(totmarks))
	print("*"*50)

#Main program
FindTotalMarks(100,"Rossum","X",English=80,Hindi=78,Telugu=65,Maths=90,Physics=60,Chemistry=58)
FindTotalMarks(200,"Travis","XII",Eng=80,Sanskrit=78,Math_1A=75,Phy=60,Che=58)
FindTotalMarks(300,"dennis","B.Tech(CSE)",OS=50,DBMS=51,NW=34)
FindTotalMarks(400,"Kinney","Research")
FindTotalMarks(500,"Trump","Politics",Politics=20,Eco=25,cnt="USA")

#Program for Demonstrating the Need of Global Variables.
#LocalGlobalVarEx1.py
def  learnAI():
	sub1="AI"  # Sub1 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
def  learnML():
	sub2="ML"  # Sub2 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub2,lang))
def  learnDL():
	sub3="DL" # Sub3 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub3,lang))
#Main Program
lang="PYTHON" # Here 'lang' is called  Global Variable
learnAI() # Function call
learnML() # Function call
learnDL() # Function call

#Program for Demonstrating the Need of Global Variables.
#LocalGlobalVarEx2.py
def  learnAI():
	sub1="AI"  # Sub1 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
def  learnML():
	sub2="ML"  # Sub2 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub2,lang))
lang="PYTHON" # Here 'lang' is called  Global Variable
def  learnDL():
	sub3="DL" # Sub3 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub3,lang))
#Main Program
learnAI() # Function call
learnML() # Function call
learnDL() # Function call

#Program for Demonstrating the Need of Global Variables.
#LocalGlobalVarEx3.py
def  learnAI():
	sub1="AI"  # Sub1 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
def  learnML():
	sub2="ML"  # Sub2 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub2,lang))
def  learnDL():
	sub3="DL" # Sub3 is Called Local Var
	print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub3,lang))
#Main Program
#learnAI() # Function call----u can't acces global var lang bcoz It defined after Function call
lang="PYTHON" # Here 'lang' is called  Global Variable
learnML() # Function call
learnDL() # Function call

#Program for Demonstrating the need of global Keyword
#GlobalKeyWordEx1.py
def  increment():
	global a
	a=a+1
def updateval():
	global a
	a=a*10
	
#main program
a=10 # here 'a' is called global variable
print("Main Program: Before Increment(),Val of a={}".format(a)) # 10
increment() # Function Call
print("Main Program: After Increment(),Val of a={}".format(a)) # 11
updateval()
print("Main Program: After updateval(),Val of a={}".format(a)) # 110

#Program for Demonstrating the need of global Keyword
#GlobalKeyWordEx2.py
def  increment():
	global a,b
	a=a+1
	b=b+1
def updateval():
	global a,b
	a=a*10
	b=b*10
	
#main program
a,b=1,2 # here 'a' and 'b' are called global variable
print("Main Program: Before Increment(), a={}  b={}".format(a,b)) # a=1 b=2
increment() # Function Call
print("Main Program: After Increment(),a={}  b={}".format(a,b)) # a=2 b=3
updateval()
print("Main Program: After updateval(),a={} b={}".format(a,b)) # a=20 b=30

#Program for Demonstrating the need of global Keyword
#GlobalKeyWordEx3.py
def  increment():
	global a,b
	a=a+1
	b=b+1
def updateval():
	global a,b
	a=a*10
	b=b*10
def modifyval():
	#Here we are just acessing global var 'a' and 'b' and need not write global keyword
	x=a+1
	y=b+1
	print("\tLocal x=",x)
	print("\tLocal y=",y)
#main program
a,b=1,2 # here 'a' and 'b' are called global variable
print("Main Program: Before Increment(), a={}  b={}".format(a,b)) # a=1 b=2
increment() # Function Call
print("Main Program: After Increment(),a={}  b={}".format(a,b)) # a=2 b=3
updateval() # Function Call
print("Main Program: After updateval(),a={} b={}".format(a,b)) # a=20 b=30
modifyval() # Function Call
print("Main Program: After modifyval(),a={} b={}".format(a,b)) # a=20 b=20

#Program for Demonstrating the need of globals() 
#In This Program both Local and Global variables Different / Unique--There is no problem in accessing them
#GlobalsFunEx1.py
a=10
b=20
c=30
d=40 # here 'a' ,'b' 'c' and 'd' are called global Variables
def   operation():
	x=100
	y=200
	z=300
	k=400 # Here 'x' ,'y' , 'z' and 'k' are called Local Variables
	res=x+y+z+k+a+b+c+d
	print("Result=",res)

#Main Program
operation() # Function Call

#Program for Demonstrating the need of globals() 
#In This Program both Local and Global variables Same--There we need to globals()
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # here 'a' ,'b' 'c' and 'd' are called global Variables
def   operation():
	a=100
	b=200
	c=300
	d=400 # Here 'a' ,'b' 'c' and 'd' are called Local Variables
	res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
	print("Result=",res)

#Main Program
operation() # Function Call

#Program for Demonstrating the need of globals() 
#GlobalsFunEx3.py
a=10
b=20 # here 'a' ,'b' are called global Variables
def   operation():
	dobj=globals()
	print("Number Global Var=",len(dobj))
	print("-"*50)
	print("Programmer + Invisible Global Variables and Values")
	print("-"*50)
	for gvn,gvv in dobj.items():
		print("\t{}-->{}".format(gvn,gvv))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-1")
	print("-"*50)
	print("\tVal of Global Var a=",dobj['a'])
	print("\tVal of Global Var b=",dobj['b'])
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-2")
	print("-"*50)
	print("\tVal of Global Var a=",dobj.get('a'))
	print("\tVal of Global Var b=",dobj.get('b'))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-3")
	print("-"*50)
	print("\tVal of Global Var a=",globals().get('a'))
	print("\tVal of Global Var b=",globals().get('b'))
	print("-"*50)
	print("Programmer-Defined Global Variables-Way-4")
	print("-"*50)
	print("\tVal of Global Var a=",globals()['a'])
	print("\tVal of Global Var b=",globals()['b'])
	print("-"*50)

#Main Program
operation() # Function Call

#Program for Accepting a Line of Text and Find the length of each word and display in the form of dict
#WordLength.py
def getlineoftext():
	return input("Enter Line of Text:")

def   findwordslength():
	line=getlineoftext() # Function call
	if (len(line)==0) or (line.isspace()):
		print("U Must Enter a Line of Text--try again")
	else:
		words=line.split()
		d={} # Create an empty Dict for adding word and its length as (key,val)
		for word in words:
			d[word]=len(word)
		else:
			for wn,wl in d.items():
				print("\t{}-->{}".format(wn,wl))
			
#Main Program
findwordslength()
