class Puzzle8(object):

    def __init__(self, lista, **kwargs):
        pai = kwargs.get('pai')
        self.lista = lista
        if pai:
            self.pai = pai


    def getLista(self):
        return self.lista


    def inOrder(self):
        anterior = -1
        for x in self.lista:
            if(x <= anterior):
                return False
            anterior = x
        return True


    def __hash__(self):
        soma = 0
        potencia = 0
        for x in self.lista:
           soma += (x+1) *(10**potencia)
           potencia = potencia + 1
        return soma


    def moves(self):
        pos = self.lista.index(0)
        movs = []
        if pos == 0:
            movs.append(self.switch(pos, 1))
            movs.append(self.switch(pos, 3))
        if pos == 1:
            movs.append(self.switch(pos, 0))
            movs.append(self.switch(pos, 2))
            movs.append(self.switch(pos, 4))
        if pos == 2:
            movs.append(self.switch(pos, 1))
            movs.append(self.switch(pos, 5))
        if pos == 3:
            movs.append(self.switch(pos, 0))
            movs.append(self.switch(pos, 4))
            movs.append(self.switch(pos, 6))
        if pos == 4:
            movs.append(self.switch(pos, 1))
            movs.append(self.switch(pos, 3))
            movs.append(self.switch(pos, 5))
            movs.append(self.switch(pos, 7))
        if pos == 5:
            movs.append(self.switch(pos, 2))
            movs.append(self.switch(pos, 4))
            movs.append(self.switch(pos, 8))
        if pos == 6:
            movs.append(self.switch(pos, 3))
            movs.append(self.switch(pos, 7))
        if pos == 7:
            movs.append(self.switch(pos, 6))
            movs.append(self.switch(pos, 4))
            movs.append(self.switch(pos, 8))
        if pos == 8:
            movs.append(self.switch(pos, 5))
            movs.append(self.switch(pos, 7))

        return movs


    def __str__(self):
         printlist = []
         printlist.extend(self.lista)
         printlist[printlist.index(0)] = ' '
         valor =('|{v0}|{v1}|{v2}|\n'+
                 '|{v3}|{v4}|{v5}|\n'+
                 '|{v6}|{v7}|{v8}|\n').format(v0=printlist[0],
                                              v1=printlist[1],
                                              v2=printlist[2],
                                              v3=printlist[3],
                                              v4=printlist[4],
                                              v5=printlist[5],
                                              v6=printlist[6],
                                              v7=printlist[7],
                                              v8=printlist[8])
         return valor


    def switch(self, v1, v2):
        temp = self.lista[v1]
        switchedList = []
        switchedList.extend(self.lista)
        switchedList[v1] = switchedList[v2]
        switchedList[v2] = temp
        return Puzzle8(switchedList, pai = self)


    def historia(self):
        try:
            hist = self.pai.historia()
            hist.append(self.lista)
            print(self)
            return hist
        except:
            print(self)
            return [self.lista]