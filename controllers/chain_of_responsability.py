from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return 'No handler found for this request.'

class HamburguesaHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Hamburguesa':
            return 'Preparando la hamburguesa.'
        else:
            return super().handle(request)

class BebidaHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Bebida':
            return 'Preparando la bebida.'
        else:
            return super().handle(request)

class PostreHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Postre':
            return 'Preparando el postre.'
        else:
            return super().handle(request)
