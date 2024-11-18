print("-----------------CLASES Y OBJETOS---------------------")

class Person: # Clase
  name = "Elioshem"

p1 = Person() # Objeto

print(p1.name)

print("-----------------METODOS Y ATRIBUTOS---------------------")

class Person: #Clase
  def __init__(self, name, age):#Metodo Constructor
    self.name = name # Atributos
    self.age = age #Atributos

  def __str__(self): #Metodo Str
    return f"{__class__.__name__}: {self.name}({self.age})"

  def myfunc(self):# 1er Metodo de objeto
    print(f"My name is {self.name}")
  

# Objeto con Atributos
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)
p1.myfunc()

#Modificar Atributos de Objeto
p1.name = "Jeshua"
print(p1.name)
p1.age = 20
print(p1.age)
print(p1)
p1.myfunc()

print("-----------------HERENCIA---------------------")

class Person: #Clase Padre
  def __init__(self, fname, lname):#Metodo Constructor
    self.firstname = fname
    self.lastname = lname

  def __str__(self): #Metodo Str
    return f"{__class__.__name__}: {self.firstname}({self.lastname})"

  def printname(self):# 1er Metodo de objeto
    print(self.firstname, self.lastname)

#Usamos la clase persona para crear un objeto, y luego ejecutamos el metodo printname:

x = Person("John", "Doe")
x.printname()

class Student(Person): # Clase Hija
  def __init__(self, fname, lname, graduationyear):#Metodo Constructor
    Person.__init__(self, fname, lname)# Atributos heredados de la clase padre
    #self.firstname = fname
    #self.lastname = lname
    self.graduationyear = graduationyear #Atributo solo de la clase hija

  def welcome(self):#Metodo de clase hija
    print(f"Welcome  {self.firstname} {self.lastname} to the class of {self.graduationyear}")

#Nota: Cuando agregamos la funcion __init__() en una clase hija, ANULAMOS la herencia __init__ de la clase Padre.
#Y para retomarla usaremos Person.__init__(self, atributo_01, atributo_02, etc), apartir del cual ya podemos crear mas atributos.
# Tambien podemos usar la funcion super().__init__(atributo_01, atributo_02), para llamar a los atributos de la clase padre. 

x = Student("Alondra", "Castillo", 2022)
x.printname()
x.welcome()

print("-----------------POLIMORFISMO---------------------")

class Person: #Clase Padre
  def __init__(self, fname, age):#Metodo Constructor
    self.firstname = fname
    self.age = age

  def actividad(self):# 1er Metodo de objeto
    print(f"No realiza ninguna actividad")

class Student(Person): # Clase Hija 01
  def actividad(self):
    print(f"El estudiante estudia")


class Maestro(Person): # Clase Hija 02
  def actividad(self):
    print(f"El maestro enseña")

class Jubilado(Person):
  pass


estudiante_01 = Student("Alondra", 12)
maestro_01 = Maestro("Pedro", 38)
jubilado_01 = Jubilado("Juan", 68)

estudiante_01.actividad()
maestro_01.actividad()
jubilado_01.actividad()