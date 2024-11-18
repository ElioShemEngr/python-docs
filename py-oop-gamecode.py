print("-----------------CLASE BASE---------------------")

class Character():
    def __init__(self, name, gender, hp, ep, level=1):
        self.name = name
        self.gender = gender
        self.hp = hp
        self.ep = ep
        self.level = level

    def attack(self):
        return self.level * 10
    
    def consume_energy(self, amount):
        if self.ep >= amount:
            self.ep -= amount
            return True
        return False 
    
    def show_stats(self):
        return {
            "Nombre": self.name,
            "Género": self.gender,
            "HP": self.hp,
            "EP": self.ep,
            "Nivel": self.level
        }
    
class Warrior(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=150, ep=50, level=level)

    def heavy_strike(self):
        """Golpe fuerte que consume energía."""
        if self.consume_energy(10):
            return self.level * 20  # Daño aumentado
        return 0  # Sin suficiente energía

class Mago(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=100, ep=100, level=level)

    def fireball(self):
        """Lanza una bola de fuego que consume energía."""
        if self.consume_energy(25):
            return self.level * 25  # Daño mágico potente
        return 0  # Sin suficiente energía

class Picaro(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=90, ep=80, level=level)

    def backstab(self):
        """Ataque furtivo que consume energía."""
        if self.consume_energy(20):
            return self.level * 30  # Daño crítico
        return 0  # Sin suficiente energía

class Healer(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=110, ep=80, level=level)

    def heal(self, target):
        """Cura a un objetivo."""
        if self.consume_energy(10):
            healing = self.level * 15
            target.heal_self(healing)
            return healing
        return 0  # Sin suficiente energía

# Creacion de Personaje
def crear_personaje():
    print("¡Bienvenido a la creación de personajes!")
    print("Elige una clase:")
    print("1. Warrior")
    print("2. Mago")
    print("3. Pícaro")
    print("4. Healer")

    # Solicitar entrada del usuario
    opcion = int(input("Ingresa el número de tu elección: "))

    # Verificar que la opción sea válida
    if opcion not in [1, 2, 3, 4]:
        print("Opción inválida. Por favor, elige entre 1 y 4.")
        return None

    # Solicitar nombre y género
    nombre = input("Ingresa el nombre de tu personaje: ")
    genero = input("Ingresa el género de tu personaje (Masculino/Femenino): ")

    # Crear personaje según la elección
    if opcion == 1:
        personaje = Warrior(name=nombre, gender=genero)
    elif opcion == 2:
        personaje = Mago(name=nombre, gender=genero)
    elif opcion == 3:
        personaje = Picaro(name=nombre, gender=genero)
    elif opcion == 4:
        personaje = Healer(name=nombre, gender=genero)

    print("\n¡Personaje creado con éxito!")
    print("Estadísticas iniciales:")
    print(personaje.show_stats())

    return personaje

# Probar la creación de personajes
if __name__ == "__main__":
    nuevo_personaje = crear_personaje()
    print(nuevo_personaje.attack())

