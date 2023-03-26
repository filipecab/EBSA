from graphics import *

import mensagensTela as ms

def sumirMensagens(win,mensagem,enter):
    
    if enter=="Return":
        mensagem.undraw()

    return mensagem

def mensagensloop(win,cont):
           
    if cont==1:
        mensagem=ms.quantidade(win)
    elif cont==2:
        mensagem=ms.destino(win)

    return mensagem
    
def loopentrada(win): 
    entrada=Entry(Point(395,350),10)
    entrada.draw(win)

    return entrada

    