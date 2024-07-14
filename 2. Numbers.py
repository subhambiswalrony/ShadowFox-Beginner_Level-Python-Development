'''
Write a function that takes two arguments, 145 and 'o', and
 uses the `format` function to return a formatted string. Print the
 result. Try to identify the representation used.
'''


def format_number(number, formatSpecifier):
    return format(number, formatSpecifier)


result = format_number(145, 'o')
print(result)

'''
 In a village, there is a circular pond with a radius of 84 meters.
 Calculate the area of the pond using the formula: Circle Area = π
 r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
 1.4 liters of water in a square meter, what is the total amount of
 water in the pond? Print the answer without any decimal point in
 it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
 Water per Square Meter
'''

pi = 3.14
radius = 84
area = pi * (radius ** 2)
print(area)

'''
If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time
'''

distance = 490
time = 7 * 60
speed = distance / time
print(int(speed))
