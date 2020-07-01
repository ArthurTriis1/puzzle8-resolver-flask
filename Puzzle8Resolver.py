from Fila import Fila
from datetime import datetime


def puzzle8Resolver(su):
    data_atual = datetime.now()
    hora = data_atual.strftime('%H:%M:%S')
    print(hora)

    hashs = set()



    fi = Fila()


    fi.add(su)

    cont = 0
    while True:

        try:
            suAnalizado = fi.remove()
        except:
            break

        if suAnalizado.inOrder() == True:
            break
        else:

            for puzzles in suAnalizado.moves():

                if (puzzles.__hash__() in hashs) == False:
                    fi.add(puzzles)

                hashs.add(puzzles.__hash__())

            cont += 1

    print('%s estados analisados, resultado:' %(cont))
    if 181441 <= cont:
        print("Formatação sem solução")
        return []
    else:
        return suAnalizado.historia()