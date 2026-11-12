
n = 6

for a in range(n):
    for b in range(n - a - 1):
        print(" ", end=" ")

    for c in range(n):
        if a == 0 or a == n - 1 or c == 0 or c == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
