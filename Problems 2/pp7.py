num_list = []

n =int(input("How many numbers in list  ? "))

for i in range(0,n):

    x=0
    y=int(input("Enter number = "))
    num_list.insert(x,y)
    x+=1

print("The list : " + str(num_list))


res = 0

for i in num_list:

	from math import pow
	res += pow(i, 2)

res = int(res)

print("The sum of squares of list is : " + str(res))
