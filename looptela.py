from graphics import *
import funcoesdiversas as fc

def loopTela(win):
    #loop de escrita na tela
    entrada=fc.loopentrada(win)
    
    while True:
        palavra=entrada.getText()
        enter=win.getKey()
        if enter=="Return":
            lista=fc.lista(palavra)
            entrada.undraw()
            entrada=fc.loopentrada(win)
            
            return enter

            
            
            
            
   

    
        

            
            