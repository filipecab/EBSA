from graphics import *

def main():
    win = GraphWin("Embarcações", 800, 600)
    win.setBackground("black")

    empresa = Text(Point(395,100), "EBSA")
    empresa.setFill("blue")
    empresa.setSize(20) 
    empresa.setStyle("bold")  
    empresa.draw(win)
    
    titulo=Text(Point(395,150),"Embracações")
    titulo.setFill("blue")
    titulo.setSize(20)
    titulo.setStyle("bold")
    titulo.draw(win)

    menu=Text(Point(395,400),"Clique - para acessar o menu")
    menu.setFill("blue")
    menu.draw(win)

    menssagem=Text(Point(395,300),"Qual a embarcação? ")
    menssagem.setFill("blue")
    menssagem.draw(win)

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
            print(palavra)
            menu=win.getKey()
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
                menssagem.undraw()
                break
        if letra=="3":
            Menu()
    
    win.getMouse() 
    win.close()

main()    


def Menu():
    win = GraphWin("Embarcações", 800, 600)
    win.setBackground("black")

    empresa = Text(Point(395,100), "EBSA")
    empresa.setFill("blue")
    empresa.setSize(20) 
    empresa.setStyle("bold")  
    empresa.draw(win)
    
    titulo=Text(Point(395,150),"Embracações")
    titulo.setFill("blue")
    titulo.setSize(20)
    titulo.setStyle("bold")
    titulo.draw(win)

    


def Quantidade():

    pass
    