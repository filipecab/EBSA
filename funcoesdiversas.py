from graphics import *

import mensagensTela as ms
import looptela as lp

#lista de objetos
listaobjetos=[]

#retorna lista
def getLista(listaobjetos1):
    listaobjetos1=listaobjetos
    return listaobjetos1

#some as mensagens na tela
def sumirMensagens(win,mensagem,enter):
    
    if enter=="Return":
        mensagem.undraw()

    return mensagem

#mensagens da tela
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
    elif cont==9:
        mensagem=ms.continuar(win)
        while True:
            enter=lp.loopTela(win)
            tamanho=len(listaobjetos)
            if enter=="Return" and listaobjetos[tamanho-1]=="1":
                cont=0
                sumir=sumirMensagens(win,mensagem,enter)
                break
            elif enter=="Return" and listaobjetos[tamanho-1]=="2":
                sumir=sumirMensagens(win,mensagem,enter)
                cont=10
                break
            
                
    return cont
    
#input de entrada 
def loopentrada(win): 
    entrada=Entry(Point(395,350),10)
    entrada.draw(win)

    return entrada

#lista de objetos
def lista(palavra):     
    listaobjetos.append(palavra)
    
    return palavra
