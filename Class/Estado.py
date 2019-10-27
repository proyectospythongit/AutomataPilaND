import Class.Pila
import sys


class EstadosImpar():
    def __init__(self, cadena, pila, error, guardar):
        self.cadena = cadena
        self.pila = pila
        self.error = error
        self.guardar = guardar
        self.estadopila = ""

    def retorno(self):
        if self.error == True:
            return True
        else:
            return False

    def devolverEstados(self):
        # print(self.guardar.mostrarEstado())
        return self.guardar.mostrarEstado()

    def devolverPila(self):
        # print(self.guardar.mostrarPila())
        return self.guardar.mostrarPila()

    def cantC(self):
        conta = 0
        for i in range(len(self.cadena)):
            if self.cadena[i] != "c":
                conta = conta + 1
            if self.cadena[i] == "c":
                break
        return conta

    def estado1(self, pila):

        self.error = True
        self.guardar.addEstado("#")
        for i in range(len(self.cadena)):
            if self.cadena[i] == "a":
                print(self.pila.tope(), self.cadena[i])
                if self.pila.tope() == "#":
                    self.pila.desapilar()
                    self.pila.apilar("#")
                    self.pila.apilar("a")
                    self.guardar.addEstado("a")

                elif self.pila.tope() == "a":
                    print("entro en tope a, letra a")
                    self.pila.desapilar()
                    self.pila.apilar("a")
                    self.pila.apilar("a")
                    self.guardar.addEstado("c")

                else:
                    self.pila.desapilar()
                    self.pila.apilar("b")
                    self.pila.apilar("a")
                    self.guardar.addEstado("e")

                print("la pila", self.pila.mostrar())
                self.estadopila = " ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Estado de la pila", self.guardar.mostrarPila())
                print("estadooooo", self.guardar.mostrarEstado())

                """print("mieruirhi",jota)"""

            if self.cadena[i] == "b":

                if self.pila.tope() == "#":
                    self.pila.desapilar()
                    self.pila.apilar("#")
                    self.pila.apilar("b")
                    self.guardar.addEstado("b")

                elif self.pila.tope() == "a":
                    self.pila.desapilar()
                    self.pila.apilar("a")
                    self.pila.apilar("b")
                    self.guardar.addEstado("d")

                else:
                    self.pila.desapilar()
                    self.pila.apilar("b")
                    self.pila.apilar("b")
                    self.guardar.addEstado("f")

                print("BBBBBBBBBBBBBBBB", "la pila", self.pila.mostrar())
                self.estadopila = " ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Estado de la pila", self.guardar.mostrarPila())
                print("estadooooo", self.guardar.mostrarEstado())

            c = self.cadena.count("c")

            if self.cadena[i] == "c":

                despuesC = (len(self.cadena) - self.cantC())

                if self.cantC() > (despuesC - 1):
                    self.error = False
                    print("palabra no es aceptada", self.error)
                    break
                j = i + 1
                if c == 1:
                    if self.pila.tope() == "#":
                        self.pila.desapilar()
                        self.guardar.addEstado("g")


                    elif self.pila.tope() == "a":
                        self.pila.desapilar()
                        self.pila.apilar("a")
                        self.guardar.addEstado("i")

                    else:
                        self.pila.desapilar()
                        self.pila.apilar("b")
                        self.guardar.addEstado("h")

                    print("CCCCCCCCCCCCCCC", "la pila", self.pila.mostrar())
                    self.estadopila = " ".join(self.pila.mostrar())
                    self.guardar.addPila(self.estadopila)
                    print("Estado de la pila", self.guardar.mostrarPila())
                    print("estadooooo", self.guardar.mostrarEstado())

                    print("la pila", self.pila.mostrar())
                    while (j < 2 * despuesC - 1):
                        print("despues", j)
                        print(self.cadena[j])
                        self.error = self.estado2(self.cadena[j])
                        # print(self.error)
                        if self.error == False:
                            break
                        else:
                            j = j + 1
                    break
                else:
                    self.error = False
                    print("palabra no es aceptada", self.error)

            if self.cadena[i] != "a" and self.cadena[i] != "b":
                self.error = False
                print("letra erronia", self.cadena[i], self.error)
                break

            if c == 0:
                self.error = False
                print("palabra no es aceptada", self.error)
                break

        return self.error

    def estado2(self, cadena):

        self.error = True

        if cadena == "c":
            print("No pasa nada")

        if cadena == "a":

            if self.pila.tope() == "a":
                self.pila.desapilar()
                print("la pila", self.pila.mostrar())
                self.guardar.addEstado("k")
                self.estadopila = " ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Estado de la pila", self.guardar.mostrarPila())
                print("estadooooo", self.guardar.mostrarEstado())

            else:

                print("palabra no es aceptada, por lo tanto no es palindroma", cadena)
                self.error = False

        if cadena == "b":

            if self.pila.tope() == "b":
                self.pila.desapilar()
                print("la pila", self.pila.mostrar())
                self.guardar.addEstado("j")
                self.estadopila = " ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Estado de la pila", self.guardar.mostrarPila())
                print("estadooooo", self.guardar.mostrarEstado())

            else:

                print("palabra no es aceptada, por lo tanto no es palindroma", cadena)
                self.error = False

        if cadena != "a" and cadena != "b" and cadena != "c":
            print(" Palabra no Aceptada, no se encuentran en el lenguaje ", cadena)
            self.error = False

        return self.error
