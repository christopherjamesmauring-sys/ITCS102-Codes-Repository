for x in range(6, 0, -1):
    for y in range(1, x+1):
        print(" ", end=" ")
    for z in range(1, 7 - x):
        print(z, end=" ")
    for a in range(5-x, 0 , -1):
        print(a,end=" ")
    print()
    