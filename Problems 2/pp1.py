
test_str = input("Enter string: ") 

res = {i: test_str.count(i) for i in set(test_str)}

print("The count of all characters is : \n" + str(res))