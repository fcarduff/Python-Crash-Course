#ordinal numbers pg 89
numbers = list(range(1,10))
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th")

# could have also been else: print(str(number) + "th")