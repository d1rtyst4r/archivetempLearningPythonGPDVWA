# Dictionaries

alien_0 = {'color': 'green', 'points': 5}  # Key : Value
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just eared " + str(new_points) + " points!")

# Add new data to dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Creating empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Changing value
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

# Changing variable value

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('x-position: ' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# Alien moving right
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('The alien new position is: ' + str(alien_0['x_position']) + '.')

# Delete key-value
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']  # Remove key and value
print(alien_0)


