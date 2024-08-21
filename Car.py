class Car():
  #Atributos
  def __init__(self, color, engine, model):
    self.color = color
    self.engine = engine
    self.model = model
  #Acciones
  def turn_on(self):
    print("The car is on")
  
  def turn_off(self):
    print("The car is off")

my_car = Car("White", "Gasoline", "Minicooper")
my_car.turn_on()
my_car.turn_off()
print(f"Color: {my_car.color}\nEngine: {my_car.engine}\nModel: {my_car.model}")

my_car.color = "Red"
my_car.engine = "Electric"
my_car.model = "Sedan"

print(f"Color: {my_car.color}\nEngine: {my_car.engine}\nModel: {my_car.model}")