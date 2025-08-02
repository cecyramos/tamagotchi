from persona import Persona
from tamagotchi import Tamagotchi

if __name__ == "__main__":
    babytchi = Tamagotchi("Babytchi", "Azul", 100, 100, 100)
    marutchi = Tamagotchi("Marutchi", "Amarillo", 100, 100, 100)
    tamatchi = Tamagotchi("Tamatchi", "Rosado", 100, 100, 100)
    mametchi = Tamagotchi("Mametchi", "Amarillo", 100, 100, 100)

    persona1 = Persona("María", "García", babytchi)
    persona2 = Persona("Pedro", "López", marutchi)
    persona3 = Persona("Luis", "García", tamatchi)
    persona4 = Persona("Ana", "Martínez", mametchi)
    
    persona1.jugar_con_tamagotchi(babytchi).darle_comida(babytchi)
    persona2.curarlo(marutchi).jugar_con_tamagotchi(marutchi)
    persona3.darle_comida(tamatchi)
    persona4.jugar_con_tamagotchi(mametchi)