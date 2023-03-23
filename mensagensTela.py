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

    enter=fc.sumirMensagens(win,p_menssagem)
    if enter=="Return":
        p_menssagem.undraw()

    return p_menssagem

def embarcacoes(win):
    embarcacao=Text(Point(395,300),"Qual a embarcação? ")
    embarcacao.setFill("blue")
    embarcacao.draw(win)

    return embarcacao

def quantidade():
    pass
