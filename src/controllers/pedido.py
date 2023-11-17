from domain.precios import PrecioTotalHandler
from controllers.hamburguesa import HamburguesaHandler
from controllers.bebida import BebidaHandler
from controllers.postre import PostreHandler
from services.pedido_builder import generar_pedido

def precios():
    precio_total_handler = PrecioTotalHandler(generar_pedido.hamburguesa, generar_pedido.bebida, generar_pedido.postre)
    print(f'Valor total: ${precio_total_handler.obtener_precio_total()}')

    hamburguesa_handler = HamburguesaHandler()
    bebida_handler = BebidaHandler()
    postre_handler = PostreHandler()

    hamburguesa_handler.set_next(bebida_handler).set_next(postre_handler)

    if generar_pedido.hamburguesa:
        print(hamburguesa_handler.handle('Hamburguesa'))
    if generar_pedido.bebida:
        print(bebida_handler.handle('Bebida'))
    if generar_pedido.postre:
        print(postre_handler.handle('Postre'))