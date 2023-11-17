from abc import ABC, abstractmethod
from domain.precios import HamburguesaPrecioHandler, BebidaPrecioHandler, PostrePrecioHandler
from views.menu import burger_choice, drink_choice, dessert_choice

class AbstractFastFood(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Hamburguesa(AbstractFastFood):
    def prepare(self):
        return f'Hamburguesa completa ${HamburguesaPrecioHandler().precio()}'

class Bebida(AbstractFastFood):
    def prepare(self):
        return f'Bebida grande ${BebidaPrecioHandler().precio()}'

class Postre(AbstractFastFood):
    def prepare(self):
        return f'Helado de chocolate ${PostrePrecioHandler().precio()}'

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

builder = FastFoodBuilder()

if burger_choice.lower() == 's':
    builder.agregar_hamburguesa(Hamburguesa())
if drink_choice.lower() == 's':
    builder.agregar_bebida(Bebida())
if dessert_choice.lower() == 's':
    builder.agregar_postre(Postre())

generar_pedido = builder.build()

if generar_pedido.hamburguesa:
    print(f'{generar_pedido.hamburguesa.prepare()}')
if generar_pedido.bebida:
    print(f'{generar_pedido.bebida.prepare()}')
if generar_pedido.postre:
    print(f'{generar_pedido.postre.prepare()}')