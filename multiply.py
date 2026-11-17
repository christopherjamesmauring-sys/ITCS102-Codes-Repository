col = int(input("Enter number of columns ---> "))

for x in range(1, 11):
    for y in range(1, col +1):
        print(x,"x",y,"=",x*y, end="\t")
    print()
    