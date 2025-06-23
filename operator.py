#  ++a   pre increment
#  a++1   post increment
a=1
c=2
b= ++a + a++1 + ++a + ++c + ++a + c++1 + a++1
print(b) # type: ignore