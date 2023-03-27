from graphics import *
import mensagensTela as ms
import looptela as lp
import funcoesdiversas as fc

#graphics py
win = GraphWin("Embarcações", 800, 600)
win.setBackground("black")

def main():
    #contagem
    cont=0
    
    #criação de tela
    ebsa=ms.logo(win)
    titulo=ms.titulo(win)
    inicio=ms.inicio(win)
    menu=ms.Menu(win)

    #escrita e mensagem
    while True:
        cont=fc.mensagensloop(win,cont)
        if cont==9:
            break 
            
            
            
    
    
    


    win.getMouse() 
    win.close()

main()    

    