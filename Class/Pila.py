class Pila():
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def tope(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items