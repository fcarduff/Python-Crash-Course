#hello admin
approved_users = ['admin', 'gunner', 'jennifer', 'archie', 'frank']
for approved_user in approved_users:
	if approved_user == 'admin':
		print(f"Hello Admin, would you like to see a status report?")
	else:
		print(f"Hello," + approved_user + ", welcome to the jungle.")

#no users pg 89
approved_users = []
if approved_users:
	for approved_user in approved_users:
		if approved_user == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello" + approved_user + ", thank you for logging in again!")
else:
	print("We need to find more users!")