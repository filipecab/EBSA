from graphics import *

import mensagensTela as ms
import looptela as lp


def sumirMensagens(win,mensagem,enter):
    
    if enter=="Return":
        mensagem.undraw()

    return mensagem

def mensagensloop(win,cont):

    if cont==0:
        mensagem=ms.embarcacoes(win) 
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
        
    elif cont==1:
        mensagem=ms.quantidade(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
        
    elif cont==2:
        mensagem=ms.destino(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==3:
        mensagem=ms.fundeioday(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==4:
        mensagem=ms.fundeiohora(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==5:
        mensagem=ms.atracacaodia(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==6:
        mensagem=ms.atracacaohora(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==7:
        mensagem=ms.saidadia(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    elif cont==8:
        mensagem=ms.saidahora(win)
        while True:
            enter=lp.loopTela(win)
            if enter=="Return":
                cont+=1
                sumir=sumirMensagens(win,mensagem,enter)
                break
    
    return cont
    
def loopentrada(win): 
    entrada=Entry(Point(395,350),10)
    entrada.draw(win)

    return entrada

    