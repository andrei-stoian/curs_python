value = int(input("Numar:\n"))

if value % 3 == 0 and value % 5 == 0:
    print("FizzBuzz")

elif value % 5 == 0:
    print("Buzz")

elif value % 3 == 0:
    print("Fizz")

else:
    print(value)