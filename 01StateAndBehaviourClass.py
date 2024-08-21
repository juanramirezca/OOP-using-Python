class LightSwitch():
  def __init__(self) -> None:
    self.switchIsOn = False

  def turn_on(self):
    self.switchIsOn = True
  
  def turn_off(self):
    self.switchIsOn = False


first_light_switch = LightSwitch()
