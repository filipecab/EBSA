from graphics import *
  
import looptela as lp

import funcoesdiversas as fc

def logo(win):
    empresa = Text(Point(395,100), "EBSA")
    empresa.setFill("blue")
    empresa.setSize(20) 
    empresa.setStyle("bold")  
    empresa.draw(win)
    return empresa
    
def titulo(win):
    titulo=Text(Point(395,150),"Embracações")
    titulo.setFill("blue")
    titulo.setSize(20)
    titulo.setStyle("bold")
    titulo.draw(win)

    return titulo

def inicio(win):
    p_menssagem=Text(Point(395,300),"Enter para iniciar!")
    p_menssagem.setFill("blue")
    p_menssagem.draw(win)

    getkey=win.getKey()
    if getkey=="Return":
        sumir=fc.sumirMensagens(win,p_menssagem,getkey)

    return p_menssagem

def Menu(win):
    menu=Text(Point(395,400),"Clique esc para acessar o menu")
    menu.setFill("blue")
    menu.draw(win)

    return menu




def embarcacoes(win):
    embarcacao=Text(Point(395,300),"Qual a embarcação? ")
    embarcacao.setFill("blue")
    embarcacao.draw(win)

    return embarcacao

def quantidade(win):
    quantidade=Text(Point(395,300),"Quantidade? ")
    quantidade.setFill("blue")
    quantidade.draw(win)

    

    return quantidade


def destino(win):
    destino=Text(Point(395,300),"Destino? ")
    destino.setFill("blue")
    destino.draw(win)
    
    return destino