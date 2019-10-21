# This program allows user to calculate the battery charge time.
import math
import local as lc

username = input(lc.NAME )
print(lc.HELLO, username, '!', sep='')
print(lc.INTRO)

# Find out the battery capacity.
battery_capacity = float(input(lc.BATTERY))
while battery_capacity < 0:
    print(lc.BATTERY1)
    battery_capacity = float(input(lc.BATTERY2))

# Find out the battery level.
charge_level = float(input(lc.CHARGE))
while charge_level < 0 or charge_level > 100:
    print(lc.CHARGE1)
    charge_level = float(input(lc.CHARGE2))

# Find out the amperage of the charger.
current_strength = float(input(lc.CURRENT))
while current_strength < 0:
    print(lc.CURRENT1)
    current_strength = float(input(lc.CURRENT2))

# Count the time.
charge_level = 100 - charge_level
charge_level = charge_level / 100
battery_capacity1 = battery_capacity * charge_level
time = 1.4 * (battery_capacity1 / (current_strength * 1000))
if time < 1:
    time = float(('{:.2f}'.format(time)))
    hours = 0
    minutes = float('{:.0f}'.format(time * 100 * 0.6))
elif time >= 1:
    time = float(('{:.2f}'.format(time)))
    hours = int(('{:.0f}'.format(time)))
    minutes = math.fabs(float('{:.0f}'.format(((time - hours) * 100 * 0.6))))

print(lc.RESULT, hours, lc.HOURS, '{:.0f}'.format(minutes), lc.MIN)

