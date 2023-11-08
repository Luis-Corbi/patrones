from abc import ABC, abstractmethod

class AbstractPrecioHandler(ABC):
    @abstractmethod
    def precio(self):
        pass

class HamburguesaPrecioHandler(AbstractPrecioHandler):
    def precio(self):
        return 5.0

class BebidaPrecioHandler(AbstractPrecioHandler):
    def precio(self):
        return 2.0

class PostrePrecioHandler(AbstractPrecioHandler):
    def precio(self):
        return 3.0

class PrecioTotalHandler:
    def __init__(self, hamburguesa, bebida, postre):
        self.hamburguesa = hamburguesa
        self.bebida = bebida
        self.postre = postre

    def obtener_precio_total(self):
        total = 0
        if self.hamburguesa:
            total += HamburguesaPrecioHandler().precio()
        if self.bebida:
            total += BebidaPrecioHandler().precio()
        if self.postre:
            total += PostrePrecioHandler().precio()
        return total
