from dao.database import conexiondb
from services.pedido_builder import generar_pedido
from dao.pedido import precios

def main():

    conexiondb

    generar_pedido

    precios()

if __name__ == "__main__":
    main()
