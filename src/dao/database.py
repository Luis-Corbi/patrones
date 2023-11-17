from dao.creacion_db import Database

db = Database('fastfood.db')
conexiondb=print(f'Base de Datos conectada: {db.database_url}')