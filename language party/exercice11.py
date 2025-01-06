nombre = [a for a in range(0,101)]
for i in nombre:
    if i%3==0 and i%5!=0:
        print("Fizz")
    if i%5==0 and i%3!=0:
        print("Buzz")
    if i%3==0 and i%5==0:
        print("FizzBuzz")
