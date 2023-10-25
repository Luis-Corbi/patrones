from domain.precios import PrecioTotalHandler
from controllers.hamburguesa import HamburguesaHandler
from controllers.bebida import BebidaHandler
from controllers.postre import PostreHandler
from services.builder import fast_food

def precios():
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