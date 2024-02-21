def soc(n):
    n-=1
    total = 0

    while n > 0:
        total += n*n*n
        n -= 1

    return total
print ("Sum of cubes smaller than the specified number: ",soc(4))