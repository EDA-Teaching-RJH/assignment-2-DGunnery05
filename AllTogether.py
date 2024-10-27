import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list:", numbers)
for number in numbers[:]:
    if number % 2 == 0:
        while number in numbers:
            numbers.remove(number)
print("List with only odd numbers:", numbers)
