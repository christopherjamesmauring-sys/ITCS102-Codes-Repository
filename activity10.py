a = 11
b = 12
c = 13

print( a > b or c < a )
print( a > b and c < a )
print( c > b and c < b )
print( c > b or c < b )

print( c > b or c < a and b == a )
print( not( c > b or c < a and b == a ))
print( b > c or a < c and b < c)
print( not( b > c or a < c and b < c))