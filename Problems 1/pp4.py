prev_num = 0 
for i in range(11):
    sum = prev_num + i
    print(f"Current Number {i} Previous Number {prev_num} sum: {sum}")
    prev_num = i
