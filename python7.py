name = input('Enter Student name :-')
age = input('Enter Student Age :-')
#sub = input ('Enter sub name:-')

Hindi=int(input('Enter your Hindi marks:-'))
English=int(input('Enter your English marks:-'))
Math=int(input('Enter your Math marks:-'))
Biology=int(input('Enter your Biology marks:-'))
History=int(input('Enter your History marks:-'))




print("Your name is - " + name)
print("your age is- "+ age)

Total = Hindi + English + Math + Biology + History

per = (Total / 500) * 100

print("your total marks is :=" + str(Total))
print(per)