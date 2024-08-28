class TV():
  def __init__(self) -> None:
    self.isOn = False
    self.isMuted = False
    self.channel_list = [2, 3, 4, 5, 7, 9, 11, 13, 20, 40]
    self.num_channels = len(self.channel_list)
    self.channel_index = 0
    self.VOLUME_MINIMUM = 0
    self.VOLUME_MAXIMUM = 10
    self.volume = 5
  
  def power(self):
    self.isOn = not self.isOn
  
  def mute(self):
    self.isMuted = not self.isMuted

  def volume_up(self):
    if not self.isOn:
      return
    if not self.isMuted:
      self.isMuted = False
    if self.volume < self.VOLUME_MAXIMUM:
      self.volume += 1

  def volume_down(self):
    if not self.isOn:
      return
    if not self.isMuted:
      self.isMuted = False
    if self.volume > self.VOLUME_MINIMUM:
      self.volume -= 1

  def channel_up(self):
    if not self.isOn:
      return
    self.channel_index += 1
    if self.channel_index > self.num_channels:
      self.channel_index = 0
      
  def channel_down(self):
    if not self.isOn:
      return
    self.channel_index -= 1
    if self.channel_index < 0:
      self.channel_index = self.num_channels - 1
  
  def set_channel(self, new_channel):
    if new_channel in self.channel_list:
      self.channel_index = self.channel_list.index(new_channel)

  def show_info(self):
    print('TV Status:')
    if self.isOn:
      print('    TV is: On')
      print('    Channel is:', self.channel_list[self.channel_index])
      if self.isMuted:
          print('    Volume is:', self.volume, '(sound is muted)')
      else:
          print('    Volume is:', self.volume)
    else:
      print('    TV is: Off')

# Main code
oTV = TV()  # create the TV object

# Turn the TV on and show the status
oTV.power()
oTV.show_info()

# Change the channel up twice, raise the volume twice, show status
oTV.channel_up()
oTV.channel_up()
oTV.volume_up()
oTV.volume_up()
oTV.show_info()

# Turn the TV off, show status, turn the TV on, show status
oTV.power()
oTV.show_info()
oTV.power()
oTV.show_info()

# Lower the volume, mute the sound, show status
oTV.volume_down()
oTV.mute()
oTV.show_info()

# Change the channel to 11, mute the sound, show status
oTV.set_channel(11)
oTV.mute()
oTV.show_info()