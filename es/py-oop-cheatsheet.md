# PYTHON OOP - CheatSheet 🐍

### 1. CLASES Y OBJETOS
```python
# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def saludar(self):  # Método de instancia
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Crear un objeto (instancia de la clase Persona)
persona1 = Persona("Juan", 30)

# Llamar al método de la clase
print(persona1.saludar())  # "Hola, me llamo Juan y tengo 30 años."
```

### 2. ENCAPSULAMIENTO
El encapsulamiento oculta los detalles internos de una clase y restringe el acceso directo a los atributos, permitiendo controlarlos a través de métodos.

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self.__saldo = saldo    # Atributo privado (no accesible directamente)

    def depositar(self, cantidad):  # Método para modificar el saldo
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):  # Método para acceder al saldo
        return self.__saldo

# Crear un objeto
cuenta = CuentaBancaria("Juan", 1000)

# Acceder al saldo mediante métodos (no directamente)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())  # 1500
cuenta.retirar(200)
print(cuenta.mostrar_saldo())  # 1300
```

### 3. HERENCIA
La herencia permite crear nuevas clases basadas en otras clases (clases padre e hijo), reutilizando y extendiendo su funcionalidad.

```python
# Clase base (padre)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass  # Método abstracto, se implementará en clases hijas

# Clase derivada (hija)
class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

# Crear objetos de clases derivadas
perro = Perro("Firulais")
gato = Gato("Michi")

# Llamar a métodos heredados y sobreescritos
print(perro.sonido())  # "Guau!"
print(gato.sonido())   # "Miau!"
```

### 4. POLIMORFISMO
El polimorfismo permite usar un mismo método o atributo de diferentes formas, dependiendo del tipo del objeto.

```python
class Ave:
    def volar(self):
        return "El ave está volando."

class Pinguino(Ave):
    def volar(self):  # Sobrescribir el método en la clase derivada
        return "Los pingüinos no vuelan."

# Función que acepta cualquier tipo de objeto que implemente el método volar
def hacer_volar(ave):
    print(ave.volar())

# Crear diferentes objetos
ave = Ave()
pinguino = Pinguino()

# Usar polimorfismo
hacer_volar(ave)       # "El ave está volando."
hacer_volar(pinguino)  # "Los pingüinos no vuelan."
```

### 5. POLIMORFISMO
La abstracción oculta detalles complejos y solo expone una interfaz clara y esencial. En Python, esto se puede lograr usando clases abstractas (disponibles en el módulo `abc`).

```python
class Ave:
    def volar(self):
        return "El ave está volando."

class Pinguino(Ave):
    def volar(self):  # Sobrescribir el método en la clase derivada
        return "Los pingüinos no vuelan."

# Función que acepta cualquier tipo de objeto que implemente el método volar
def hacer_volar(ave):
    print(ave.volar())

# Crear diferentes objetos
ave = Ave()
pinguino = Pinguino()

# Usar polimorfismo
hacer_volar(ave)       # "El ave está volando."
hacer_volar(pinguino)  # "Los pingüinos no vuelan."
```

### 6. ABSTRACCION
Los métodos y atributos de clase son compartidos por todas las instancias de una clase.

```python
class Producto:
    # Atributo de clase
    iva = 0.21  # IVA del 21%

    def __init__(self, nombre, precio):
        self.nombre = nombre  # Atributo de instancia
        self.precio = precio  # Atributo de instancia

    # Método de clase (modifica el atributo de clase)
    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        cls.iva = nuevo_iva

    # Método para calcular el precio final con IVA
    def precio_final(self):
        return self.precio * (1 + Producto.iva)

# Crear una instancia de Producto
producto = Producto("Laptop", 1000)
print(producto.precio_final())  # 1210.0 (con IVA del 21%)

# Cambiar el IVA a través de un método de clase
Producto.cambiar_iva(0.18)
print(producto.precio_final())  # 1180.0 (con IVA del 18%)
```

### 7. METODOS Y ATRIBUTOS ESTATICOS
Los métodos estáticos son funciones dentro de una clase que no acceden ni modifican el estado de la clase o la instancia. Se utilizan para funciones relacionadas lógicamente con la clase, pero que no dependen de ella.

```python
class Matematica:
    @staticmethod
    def suma(a, b):
        return a + b

# No es necesario crear una instancia para llamar a un método estático
resultado = Matematica.suma(5, 3)
print(resultado)  # 8
```

### 8. HERENCIA MULTIPLE
Python permite que una clase herede de múltiples clases. Esto permite compartir funcionalidades entre clases no relacionadas.

```python
class Mamifero:
    def caminar(self):
        return "El mamífero camina."

class Ave:
    def volar(self):
        return "El ave vuela."

# Clase que hereda de Mamifero y Ave
class Murcielago(Mamifero, Ave):
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia de Murciélago
murcielago = Murcielago("Bruce")

# Acceder a métodos de ambas clases
print(murcielago.caminar())  # "El mamífero camina."
print(murcielago.volar())    # "El ave vuela."
```

### 9. METODOS ESPECIALES
Los métodos especiales en Python (conocidos como dunders) permiten definir comportamientos personalizados para operadores y funciones comunes, como la representación de objetos o la sobrecarga de operadores.

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecargar el operador suma (+)
    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

    # Representación en string del objeto
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

# Crear dos puntos
punto1 = Punto(2, 3)
punto2 = Punto(4, 5)

# Usar el operador + (sobrecargado)
resultado = punto1 + punto2
print(resultado)  # Punto(6, 8)
```

### 10. COMPOSICION
La composición implica que un objeto "contiene" otro objeto como parte de su estado. Esto permite crear relaciones de tipo "tiene un" entre objetos.

```python
class Motor:
    def encender(self):
        return "Motor encendido."

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor()  # El coche contiene un motor

    def arrancar(self):
        return f"{self.marca}: {self.motor.encender()}"

# Crear un coche
coche = Coche("Toyota")
print(coche.arrancar())  # "Toyota: Motor encendido."
```

