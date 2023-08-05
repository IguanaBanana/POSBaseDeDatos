#Konomi Code
from tkinter import *
import tkinter.messagebox
import apiBusacar
from PIL import Image, ImageTk

codigo=''
def key_pressed(event):
    global codigo
    if event.keysym== 'Return':
        #print(event.keys.ym)
        print('Buscando producto con codigo: ' + codigo)
        codigo=''
    else:
        codigo+= event.keysym
ventana=Tk()
ventana.title('Verificador de Precios')
ventana['bg']='#DE2E03'
ventana.geometry('500x500')


ventana.bind('<Key>', key_pressed)
ventana.mainloop()