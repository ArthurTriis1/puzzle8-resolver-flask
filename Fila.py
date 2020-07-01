class Fila(object):
    
    def __init__(self):
        self.fila = []
    
    def add(self, adicionar):
        self.fila.append(adicionar)
    def remove(self):

        return self.fila.pop(0)

    def length(self):
        return len(self.fila)