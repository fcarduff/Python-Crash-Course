alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"Congratulations you just earned {new_points} points!")
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
print(f"The alien is {alien_0['color']}.")
alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#move alien to the right
#determine how far to move alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#this must be fast alien
	x_increment = 3 
#the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.")