requested_toppings = ['olives']
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
		print("\nFinished making your pizza!")	
else:
	print("Are you sure you want a plain pizza?")
#nevermind got it working
#had if and else at different indentations, should have been the same