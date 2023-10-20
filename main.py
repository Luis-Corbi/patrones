from services.singleton import Database
from models.builder import FastFoodBuilder, Hamburguesa, Bebida, Postre
from models.precios import PrecioTotalHandler
from controllers.chain_of_responsability import HamburguesaHandler, BebidaHandler, PostreHandler

def main():

    db = Database('fastfood.db')
    print(f'Base de Datos conectada: {db.database_url}')

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

    precio_total_handler = PrecioTotalHandler(fast_food.hamburguesa, fast_food.bebida, fast_food.postre)
    print(f'Valor total: {precio_total_handler.obtener_precio_total()}')

    hamburguesa_handler = HamburguesaHandler()
    bebida_handler = BebidaHandler()
    postre_handler = PostreHandler()

    hamburguesa_handler.set_next(bebida_handler).set_next(postre_handler)

    if fast_food.hamburguesa:
        print(hamburguesa_handler.handle('Hamburguesa'))
    if fast_food.bebida:
        print(bebida_handler.handle('Bebida'))
    if fast_food.postre:
        print(postre_handler.handle('Postre'))

if __name__ == "__main__":
    main()
