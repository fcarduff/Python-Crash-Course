#checking usernames pg 89
current_users = ['archie', 'gunner', 'jennifer', 'frank', 'pandy']
new_users = ['archie', 'spongebob', 'sandy', 'PANDY', 'patrick']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users:
		print("This username is already taken, please select a new username")
	else:
		print(f"Welcome " + new_user + ", thank you for logging in!")

#This case insensitivity was kinda hard tbh