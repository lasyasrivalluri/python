print(10+20)
print(10-15)
print(2*3)
print(5/2)
print(5%2)
print(2**3)
print(5//2)
#Assignment Operators
x = 5
print(x)#x lo 5 ni store chasukukuntadhi
x += 3 # line number 9 lo unna x ki line number 11 lo unna number add avuthadhi 
print(x)
x -= 2 # line number 9 lo unna x ki line number 13 lo unna number sub avthadhi
print(x)
x *= 2
print(x)
x=5
x %=3
print(x)
                          #  4 2 1
x=5 #  binary representation(1 0 1)
x &= 3 # binary representatin(0 1 1)
        #------------------------------
        #                      0 0 1
print(x)# x valu anadhi 1 ani vasthadhi

x = 5#  binary representation(1 0 1)
x |= 3# binary representatin(0 1 1)
        #------------------------------
        #                      1 1 1   (4+2+1)
print(x)# x valu anadhi 7 ani vasthadhi

x = 5
x ^= 3
print(x)

x = 5
x >>= 2
print(x)
x = 5
x <<= 3
print(x)

x=5
y=5
print(x==y)

x=5
y=5
print(x!=y)

x=5
y=10
print(x<=y)
#logical operaters
x = 5
print(x > 3 and x < 10)# if both statements are true returns true

x = 5
print(x > 3 and x < 10)# if both statements are true returns true
#identity operater
x=["lasya","sree"]
y=["valluri"]
print(x is not y)

x=["lasya","sree"]
x=["valluri"]
print(x is  x)