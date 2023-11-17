from domain.handlers_abstract import AbstractHandler

class PostreHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Postre':
            return 'Preparando el postre.'
        else:
            return super().handle(request)