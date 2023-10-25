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

builder = FastFoodBuilder()

burger_choice = input("¿Desea agregar una hamburguesa a su pedido? (s/n): ")
drink_choice = input("¿Desea agregar una bebida a su pedido? (s/n): ")
dessert_choice = input("¿Desea agregar un postre a su pedido? (s/n): ")

if burger_choice.lower() == 's':
    builder.agregar_hamburguesa(Hamburguesa())
if drink_choice.lower() == 's':
    builder.agregar_bebida(Bebida())
if dessert_choice.lower() == 's':
    builder.agregar_postre(Postre())

fast_food = builder.build()

if fast_food.hamburguesa:
    print(f'{fast_food.hamburguesa.prepare()}')
if fast_food.bebida:
    print(f'{fast_food.bebida.prepare()}')
if fast_food.postre:
    print(f'{fast_food.postre.prepare()}')