numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.pop(0)
numbers += numbers.copy()
numbers.insert(3, 25)
print(numbers)
