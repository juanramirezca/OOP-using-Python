"""
This script shows the state and behavior of a switch, that can be either
on or off.
Note that we will need to use the global keyword
"""
def turnOn():
  switch_is_on
  switch_is_on = True

def turnOff():
  switch_is_on
  switch_is_on = False

switch_is_on = False

print(switch_is_on)
turnOn()
print(switch_is_on)
turnOff()
print(switch_is_on)
turnOn()
print(switch_is_on)