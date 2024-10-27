# PYTHON Basics - CheatSheet 🐍

### 1. COMENTARIOS
```python
# Este es un comentario en una linea

'''
Este es un
comentario
en multiples
lineas
'''
```

### 2. VARIABLES Y TIPOS DE DATOS
```python
# Declaración de variables
nombre = "Juan"  # String
edad = 30        # Entero (int)
altura = 1.75    # Flotante (float)
es_estudiante = True  # Booleano

# Imprimir variables
print(nombre, edad, altura, es_estudiante)

# Verificar tipo de dato
print(type(nombre))  # <class 'str'>
print(type(edad))    # <class 'int'>
print(type(altura))  # <class 'float'>
```

### 3. OPERADORES BASICOS

```python
# Operadores aritméticos
suma = 5 + 3           # Suma -> 8
resta = 5 - 3          # Resta -> 2
multiplicacion = 5 * 3 # Multiplicación -> 15
division = 5 / 3       # División -> 1.6666...
modulo = 5 % 3         # Residuo -> 2
potencia = 5 ** 3      # Potencia -> 125

# Operadores de comparación
es_mayor = 5 > 3       # True
es_igual = 5 == 3      # False
es_distinto = 5 != 3   # True

# Operadores lógicos
es_verdad = True and False  # False
es_falso = not True         # False
```

### 4. CONDICIONALES(`if`,`elif`,`else`)
```python
edad = 20

# Condicional simple
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Condicional con múltiples opciones
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Bueno")
else:
    print("Necesita mejorar")
```

## 5. BUCLES(`for`,`while`)
```python
# Bucle `for` para iterar sobre una lista
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print(fruta)

# Bucle `for` con `range`
for i in range(5):  # De 0 a 4
    print(i)

# Bucle `while`
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incremento en cada iteración
```

## 6. FUNCIONES
```python
# Definición de una función simple
def saludar(nombre):
    return f"Hola, {nombre}!"

# Llamada a la función
print(saludar("Juan"))

# Función con múltiples parámetros
def sumar(a, b):
    return a + b

print(sumar(5, 3))  # 8
```

## 7. LISTAS
```python
# Creación de listas
numeros = [1, 2, 3, 4, 5]

# Acceso a elementos
print(numeros[0])  # Primer elemento -> 1
print(numeros[-1]) # Último elemento -> 5

# Modificar un elemento
numeros[0] = 10

# Métodos de listas
numeros.append(6)  # Agrega un elemento al final
numeros.remove(3)  # Elimina el primer elemento que coincide con 3
numeros.pop()      # Elimina y devuelve el último elemento

# Slicing de listas
print(numeros[1:4])  # Sublista desde el índice 1 al 3
```

## 8. DICCIONARIOS
```python
# Creación de diccionarios
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Acceso a elementos
print(persona["nombre"])  # Juan

# Modificar un valor
persona["edad"] = 31

# Añadir una nueva clave-valor
persona["profesión"] = "Ingeniero"

# Métodos de diccionarios
print(persona.keys())    # Todas las claves
print(persona.values())  # Todos los valores
```

## 9. TUPLAS
```python
# Creación de tuplas (inmutables)
coordenadas = (10, 20)

# Acceso a elementos
print(coordenadas[0])  # 10

# Las tuplas no se pueden modificar, pero pueden contener listas
```

## 10. SETS
```python
# Creación de un conjunto
numeros = {1, 2, 3, 4, 5}

# Añadir un elemento
numeros.add(6)

# Eliminar un elemento
numeros.remove(1)

# Operaciones de conjuntos
otros_numeros = {4, 5, 6, 7}
union = numeros.union(otros_numeros)       # Unión
interseccion = numeros.intersection(otros_numeros)  # Intersección
```

## 11. EXCEPCIONES
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
finally:
    print("Este bloque se ejecuta siempre.")
```

## 12. LIST COMPREHENSIONES
```python
# Crear una nueva lista basada en otra lista
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]

# List comprehension con condicional
pares = [x for x in numeros if x % 2 == 0]
```

## 13. FUNCIONES LAMBDA
```python
# Función lambda para sumar dos números
suma = lambda x, y: x + y
print(suma(2, 3))  # 5

# Uso de lambda con `map`
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
```

## 14. CLASES Y OBJETOS
```python
# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Crear un objeto
persona1 = Persona("Juan", 30)

# Llamar a un método
print(persona1.saludar())
```

## 15. MODULOS Y PAQUETES
```python
# Importar un módulo
import math

# Usar funciones de un módulo
print(math.sqrt(16))  # Raíz cuadrada -> 4.0

# Importar una función específica
from math import pi
print(pi)  # 3.14159
```

## 16. LECTURA Y ESCRITURA DE ARCHIVOS
```python
# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!")

# Leer un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

## 17. DECORADORES
```python
# Definir un decorador
def mi_decorador(func):
    def envoltura():
        print("Antes de la función.")
        func()
        print("Después de la función.")
    return envoltura

@mi_decorador
def funcion_ejemplo():
    print("Función en ejecución.")

# Llamar a la función decorada
funcion_ejemplo()
```

## 18. GENERADORES
```python
# Definir un generador
def contador():
    i = 0
    while i < 5:
        yield i
        i += 1

# Usar el generador
for numero in contador():
    print(numero)
```

## 19. EXPRESIONES REGULARES
```python
import re

# Buscar una coincidencia
texto = "Mi número es 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)

if resultado:
    print("Número encontrado:", resultado.group())
```

## 20. CONTEXTS MANAGERS
```python
# Uso de un context manager para asegurar el cierre de un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Este archivo se cierra automáticamente.")
```