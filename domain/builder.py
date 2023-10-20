from abc import ABC, abstractmethod

class AbstractFastFood(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Hamburguesa(AbstractFastFood):
    def prepare(self):
        return 'Hamburguesa completa'

class Bebida(AbstractFastFood):
    def prepare(self):
        return 'Bebida grande'

class Postre(AbstractFastFood):
    def prepare(self):
        return 'Helado de chocolate'

class FastFoodBuilder:
    def __init__(self):
        self.producto = FastFood()

    def agregar_hamburguesa(self, hamburguesa):
        self.producto.hamburguesa = hamburguesa
        return self

    def agregar_bebida(self, bebida):
        self.producto.bebida = bebida
        return self

    def agregar_postre(self, postre):
        self.producto.postre = postre
        return self

    def build(self):
        return self.producto

class FastFood:
    def __init__(self):
        self.hamburguesa = None
        self.bebida = None
        self.postre = None