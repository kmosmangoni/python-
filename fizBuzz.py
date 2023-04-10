def fizzbuzz(x,t):
    for i in range(1,100):
      if i % x == 0 and i % t == 0:
        print("fizzbuzz")        
      elif i % x == 0:
        print("fizz")        
      elif i % t == 0:
        print("buzz")        
    print(i)
fizzbuzz(9,7)