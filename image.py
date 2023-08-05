from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("imagen")
ventana.geometry('500x500')
#Creamos Variable para la imagen
try:
    image = Image.open("./img/changuish.jpg")
    image= image.resize((300,300))
    Test= ImageTk.PhotoImage(image)
    lbl_codigo= Label(ventana, image=Test)

except:
    lbl_codigo = Label(ventana, text='imagen no disponible')

#labels
lbl_codigo.pack(pady=20)
ventana.mainloop()