from tamagotchi import Tamagotchi
class Persona:
    def __init__(self, nombre, apellido, tamagotchi: Tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self, tamagotchi):
        self.tamagotchi.jugar()
        print(f"{self.nombre} está jugando con {tamagotchi.nombre}")
        return self
    def darle_comida(self, tamagotchi):
        self.tamagotchi.comer()
        print(f"{self.nombre} le está dando comida a {tamagotchi.nombre}")
        return self
    def curarlo(self, tamagotchi):
        self.tamagotchi.curar()
        print(f"{self.nombre} está curando a {tamagotchi.nombre}")
        return self