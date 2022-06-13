guests = ['hambone', 'babe', 'archibald', 'spongebob', 'patrick' ]
print('I can only invite 2 guests to Dinner tomorrow. I do apologize.')
popped_1 = guests.pop(3)
message_2 = f"Sorry {popped_1.title()}, I am unable to accomodate you for Dinner tomorrow."
print(message_2)
popped_2 = guests.pop(2)
message_3 = f"Sorry {popped_2.title()}, I am unable to accomodate you for Dinner tomorrow"
print(message_3)
popped_3 = guests.pop(2)
message_4 = f'Sorry {popped_3.title()}, I am unable to accomodate you for Dinner tomorrow'
print(message_4)
message_5 = f"Hey {guests[0].title()} and {guests[1].title()}, just letting you know we are still on for tomorrow!!!"
print(message_5)
print(len(guests))