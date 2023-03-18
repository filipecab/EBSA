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

    win.getMouse() 
    win.close()
        

main()    


    