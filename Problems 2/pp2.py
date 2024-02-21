def maxn(a,b,c):

    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("largest number is ",maxn(a, b, c))