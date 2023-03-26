from graphics import *
import mensagensTela as ms
import looptela as lp
import funcoesdiversas as fc

#graphics py
win = GraphWin("Embarcações", 800, 600)
win.setBackground("black")

def main():
    #contagem
    cont=1
    
    #criação de tela
    ebsa=ms.logo(win)
    titulo=ms.titulo(win)
    inicio=ms.inicio(win)
    menu=ms.Menu(win)

    embarcacao=ms.embarcacoes(win)

    while True:
        enter=lp.loopTela(win)
        if enter=="Return":
            embarcacao.undraw()
            mensagem=fc.mensagensloop(win,cont)
            cont+=1
            
    
    
    


    win.getMouse() 
    win.close()

main()    

    