from graphics import *
  
import looptela as lp

import funcoesdiversas as fc


#todas as mensagens da tela

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
    else:
        while getkey!="Return":
            getkey=win.getKey()
            if getkey=="Return":
                sumir=fc.sumirMensagens(win,p_menssagem,getkey)
                break
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

def fundeioday(win):
    fundeiodia=Text(Point(395,300),"Fundeio dia? dia/mes/ano")
    fundeiodia.setFill("blue")
    fundeiodia.draw(win)

    return fundeiodia

def fundeiohora(win):
    fundeiohora=Text(Point(395,300),"Fundeio hora? hora:minuto")
    fundeiohora.setFill("blue")
    fundeiohora.draw(win)

    return fundeiohora

def atracacaodia(win):
    atracacaodia=Text(Point(395,300),"Atracação dia? dia/mes/ano")
    atracacaodia.setFill("blue")
    atracacaodia.draw(win)

    return atracacaodia

def atracacaohora(win):
    atracacaohora=Text(Point(395,300),"Atracação hora? hora:minuto")
    atracacaohora.setFill("blue")
    atracacaohora.draw(win)

    return atracacaohora

def saidadia(win):
    saidadia=Text(Point(395,300),"Saida dia? dia/mes/ano")
    saidadia.setFill("blue")
    saidadia.draw(win)

    return saidadia


def saidahora(win):
    saidahora=Text(Point(395,300),"Saida hora? hora:minuto")
    saidahora.setFill("blue")
    saidahora.draw(win)

    return saidahora

def continuar(win):
    continua=Text(Point(395,300),"Digite 1 para digitar outra linha e 2 para parar")
    continua.setFill("blue")
    continua.draw(win)

    return continua