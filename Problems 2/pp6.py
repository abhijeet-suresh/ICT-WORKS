num = []
n =int(input("How many numbers ? "))
for i in range(0,n):
    x=0
    y=int(input("Enter number = "))
    num.insert(x,y)
    x+=1
def freq(num):
    return max(set(num), key = num.count)
print(freq(num))