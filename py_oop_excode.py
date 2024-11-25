print("-----------------CLASES Y OBJETOS---------------------")

class NombreClase():
    pass

nombreObjeto = NombreClase()

print("-----------------METODOS Y ATRIBUTOS---------------------")

class NombreClase():
    atributo01 = "valor 1"
    atributo02 = "valor 2"

    def metodo_1(self):
        print("metodo de clase 1")

    def metodo_2(self):
        print("metodo de clase 2")

nombreObjeto = NombreClase()

print(nombreObjeto.atributo01)
nombreObjeto.metodo_1()

print("-----------------HERENCIA---------------------")

class HerenciaClase(NombreClase):
    pass

nombreObjeto02 = HerenciaClase()

print(nombreObjeto.atributo02)
nombreObjeto.metodo_2()


print("-----------------POLIMORFISMO---------------------")

class HerenciaClase02(NombreClase):
    pass

    def metodo_2(self):
        print("Metodo con polimorfismo")

nombreObjeto03 = HerenciaClase02()

print(nombreObjeto03.atributo02)
nombreObjeto03.metodo_2()
