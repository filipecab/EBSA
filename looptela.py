from graphics import *

import mensagensTela as ms
import funcoesdiversas as fc

def loopTela(win):


    #listas de objetos
    embarcacaolist=[]
    quantidadelist=[]
    destinolist=[]
    fundeiodialist=[]
    fundeiohoralist=[]
    atracacaodialist=[]
    atracacaohoralist=[]
    saidadialist=[]
    saidahoralist=[]
    
    
    #loop de escrita na tela
    entrada=fc.loopentrada(win)
    
    while True:
        palavra=entrada.getText()
        enter=win.getKey()
        if enter=="Return":
            entrada.undraw()
            entrada=fc.loopentrada(win)
            return enter

            
            
            
            
   

    
        

            
            