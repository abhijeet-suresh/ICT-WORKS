
for fizzbuzz in range(1,11):
    
    if fizzbuzz % 2 == 0 and fizzbuzz % 5 == 0:
       
        print("fizzbuzz")
        continue

    elif fizzbuzz % 2 == 0:
       
        print("fizz")
        continue

    elif fizzbuzz % 5 == 0:
       
        print("buzz")
        continue
  
    print(fizzbuzz) 
	