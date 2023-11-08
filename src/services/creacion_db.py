from abc import ABCMeta, abstractmethod

class SingletonMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AbstractDatabase(metaclass=SingletonMeta):
    @abstractmethod
    def connect(self):
        pass

class Database(AbstractDatabase):
    def __init__(self, database_url):
        self.database_url = database_url

    def connect(self):
        pass