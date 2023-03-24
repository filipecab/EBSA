from graphics import *
import mensagensTela as ms
import looptela as lp
import funcoesdiversas as fc



#listas de objetos
embarcacao=[]
quantidade=[]
destino=[]
fundeiodia=[]
fundeiohora=[]
atracacaodia=[]
atracacaohora=[]
saidadia=[]
saidahora=[]

#graphics py
win = GraphWin("Embarcações", 800, 600)
win.setBackground("black")

def main():
    #criação de tela
    ebsa=ms.logo(win)
    titulo=ms.titulo(win)
    inicio=ms.inicio(win)
    menu=ms.Menu(win)
    lp.loopTela(win)    
    
    


    win.getMouse() 
    win.close()

main()    

    