"""
This is a more complicated example of using a class.
A class would have to mainting the following data:
* Power state (on or off)
* Mute state (is it muted?)
* List of channels available
* Current channel setting
* Current volume setting
* Range of volume levels available.

And the actions must include:
* Turn the power on and off
* Raise and lower the volume
* Change the channel up and down
* Mute and unmute the sound
* Get information about the current settings
* Go to a specified channel

"""

class Television():
  def __init__(self):
    self.power = False
    self.mute = False
    self.channel = 1
    self.volume = 0

  def turn_power(self):
    if self.power == True:
      self.power = False
    else:
      self.power = True
    self.power_on_off()
  
  def power_on_off(self):
    if self.power == True:
      print("Power is ON")
    else: 
      print("Power is OFF")
  
  def mute_and_unmute(self):
    if self.mute == True:
      self.mute = False
    else:
      self.mute = True
    self.mute_state()
  
  def mute_state(self):
    if self.mute == True:
      print("Muted")
    else:
      print("Unmuted")

  def raise_volume(self):
    if self.volume < 10:
      self.volume += 1
    self.show_volume()

  def lower_volume(self):
    if self.volume > 0:
      self.volume -= 1
    self.show_volume()
  
  def show_volume(self):
    print(f"Volume: {self.volume}")

  def channel_up(self):
    if self.channel < 100:
      self.channel += 1
    self.show_channel()
  
  def channel_down(self):
    if self.channel > 1:
      self.channel -= 1
    self.show_channel()

  def show_channel(self):
    print(f"Channel: {self.channel}")
  
  def go_to_channel(self, channel_num):
    if channel_num > 1 and channel_num < 100:
      self.channel = channel_num
    self.show_channel()

  
myTelevision = Television()
myTelevision.go_to_channel(35)
myTelevision.channel_up()
myTelevision.raise_volume()
myTelevision.raise_volume()
myTelevision.raise_volume()
myTelevision.mute_and_unmute()
myTelevision.mute_and_unmute()
myTelevision.mute_and_unmute()
myTelevision.turn_power()
myTelevision.turn_power()
myTelevision.turn_power()



  



  