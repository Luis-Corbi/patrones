from services.singleton import Database

db = Database('fastfood.db')
data=print(f'Base de Datos conectada: {db.database_url}')