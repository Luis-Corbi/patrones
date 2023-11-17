from dao.database import conexiondb
from services.pedido_builder import generar_pedido
from controllers.pedido import generar_precio_total

def main():

    conexiondb

    generar_pedido

    generar_precio_total()

if __name__ == "__main__":
    main()
