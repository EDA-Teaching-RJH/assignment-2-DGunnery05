numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()
numbers2 = [num for num in numbers if num != 1]
numbers2.extend([7, 8])
print(numbers2)
