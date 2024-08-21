# Atributos
# name, color, race, complexion
# Acciones
# maullar, caminar, attack

class Cat():
  def __init__(self, name, color, race, paws):
    self.name = name
    self.color = color
    self.race = race
    self.paws = paws
  
  def maullar(self):
    print("Miauuuuu")

  def caminar(self):
    print("Caminando ...")

  def atacar(self):
    print("El gato te está atacando!!!")


michi = Cat("Michi", "Naranja", "Naranjoso", 4)
michi.maullar()
michi.caminar()
michi.atacar()


# Tarea: Crear una clase llamada Dog, Book