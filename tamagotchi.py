class Tamagotchi:
    def __init__(self, nombre, color, felicidad, salud, energia):
        self.nombre = nombre
        self.color = color
        self.felicidad = felicidad
        self.salud = salud
        self.energia = energia
    def jugar(self): #jugar(): incrementa la felicidad el 10, disminuye la salud en 5
        if self.felicidad == 100:
            self.felicidad = 100
            print(f"{self.nombre} ya está feliz")
        elif self.felicidad >= 90:
            self.felicidad = 100
            print(f"{self.nombre} ahora está muy feliz")
        else:
            self.felicidad += 10
        if self.salud == 0:
            self.salud = 0
            print(f"{self.nombre} ya está muerto x.x")
        elif self.salud <= 5:
            self.salud = 0
            print(f"Acabas de matar a {self.nombre} x.x")
        else:
            self.salud -= 5
        print(f"La felicidad de {self.nombre} es {self.felicidad} y su salud es {self.salud}")
    def comer(self): #comer(): incrementa la felicidad en 5, aumenta la salud en 10
        if self.felicidad == 100:
            self.felicidad = 100
            print(f"{self.nombre} ya está feliz")
        elif self.felicidad >= 95:
            self.felicidad = 100
            print(f"{self.nombre} ahora está muy feliz")
        else:
            self.felicidad += 5
        if self.salud == 100:
            self.salud = 100
            print(f"{self.nombre} ya está saludable")
        elif self.salud >= 90:
            self.salud = 100
            print(f"{self.nombre} ahora está muy saludable")
        else:
            self.salud += 10
        print(f"La felicidad de {self.nombre} es {self.felicidad} y su salud es {self.salud}")
    def curar(self): #curar(): incrementa la salud en 20, disminuye la felicidad en 5
        if self.salud == 100:
            self.salud = 100
            print(f"{self.nombre} ya está saludable")
        elif self.salud >= 80:
            self.salud = 100
            print(f"{self.nombre} ahora está muy saludable")
        else:
            self.salud += 20
        if self.felicidad == 0:
            self.felicidad = 0
            print(f"{self.nombre} es muy infeliz (˚ ˃̣̣̥⌓˂̣̣̥ )")
        elif self.felicidad <= 5:
            self.felicidad = 0
            print(f"Acabas de haer a {self.nombre} muy triste .·°՞(っ-ᯅ-ς)՞°·.")
        else:
            self.felicidad -= 5
        print(f"La felicidad de {self.nombre} es {self.felicidad} y su salud es {self.salud}")