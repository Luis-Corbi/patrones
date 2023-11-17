from domain.handlers import AbstractHandler

class HamburguesaHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Hamburguesa':
            return 'Preparando la hamburguesa.'
        else:
            return super().handle(request)