a=10 #int
print(a)
type(a)
id(a)
print(a,type(a),id(a))
a=10
b=20
c=a+b
print(a,type(a),id(a))
print(b,type(b),id(b))
print(c,type(c),id(c))
# Numeric Types in Python
a=0b1001 #binary
print(a,type(a))
a=0B1111
print(a,type(a))
a=0B10000
print(a,type(a))

a=0o17#0ctal
print(a,type(a))
a=0o14
print(a,type(a))
a=0o123
print(a,type(a))

a=0xac #hexadecimal
print(a,type(a))
a=0XBEE
print(a,type(a))


a=1.2#flaot
print(a,type(a))
a=2.2
b=2.3
c=a+b
print(a,type(a))
print(b,type(b))
print(c,type(c))
a=2 
b=2.5
c=a+b
print(a,type(a))
print(b,type(b))
print(c,type(c))
a=3e2
print(a,type(a))
b=10e-2
print(b,type(b))


#bool
a=True
b=False
c=a+b
print(c,type(c))
print(2+True-False)
print(2+True*4)
print(0b1111-True)
print(0xF+True)
print(0o7+True)
print(0b1111+False)
print(False/True)


#complex
a=2+3j
print(a,type(a))
b=-2-3.5j
print(b,type(b))
c=1.5-4.5j
print(c,type(c))
d=3j
print(d,type(d))
e=3.5j
print(e,type(e))
a=2+3j
print(a,type(a))
print(a.real)
print(a.imag)
a=2+3.5j
print(a.real)
print(a.imag)





