from graphics import *

import mensagensTela as ms

def loopTela(win):
    

    embarcacao=ms.embarcacoes(win)

    entrada=Entry(Point(395,350),10)
    entrada.draw(win)
    txt=Text(Point(1,1),"")
    txt.setFill("black")
    txt.draw(win)

    while True:
        txt.setText(entrada.getText())
        palavra=entrada.getText()
        letra=win.getKey()
        if letra=="Return":
            entrada.undraw()
            continuar=Text(Point(395,350),"Deseja digitar outra palavra 1 sim, 2 não")
            continuar.setFill("blue")
            continuar.draw(win)
            letra=win.getKey()
            if letra=="1":
                continuar.undraw()
                entrada=Entry(Point(395,350),10)
                entrada.draw(win)
    
            elif letra=="2":
                continuar.undraw()
                embarcacao.undraw()
                break