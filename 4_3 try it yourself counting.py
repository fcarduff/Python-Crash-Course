for value in range(1,21,1):
	print(value)
numbers = list(range(1,1000000))
print(numbers)
#that was awesome
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

divisible_3 = list(range(3,30,3))
print(divisible_3)

cubes = [value**3 for value in range(1,10)]
print(list(cubes))