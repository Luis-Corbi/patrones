from controllers.chain import AbstractHandler

class BebidaHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Bebida':
            return 'Preparando la bebida.'
        else:
            return super().handle(request)