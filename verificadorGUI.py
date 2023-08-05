#Verificador GUI Api Completo
from tkinter import *
import apiBusacar
import tkinter.messagebox
from PIL import Image, ImageTk

codigo=''
def key_pressed(event):
    global codigo
    if event.keysym== 'Return':
        llamadaDatos(codigo)
        codigo=''
    else:
        codigo+= event.keysym

def llamadaDatos(codigo):
    try:
        resultado = apiBusacar.buscarProducto(codigo)
        if resultado == 0:
            resultado.config(text="No se localizó el código del producto " + codigo)
        elif resultado == -1:
            resultado.config(text='Error en la conexión')
        else:
            lbl_resultado.config(text='Nombre del Producto: ' + str(resultado[1]) + "\n" + 'Precio: '
                                 + str(resultado[2]))
            if hasattr(llamadaDatos, 'imagen_label'):
                llamadaDatos.imagen_label.destroy()
                img = Image.open("." + resultado[3]) #llamamos la imagen. 
                img = img.resize((150, 150))  # Ajusta el tamaño de la imagen si es necesario
                img_tk = ImageTk.PhotoImage(img) #usamos la propiedad para poder cargar el pad de la imagen. 
                imagen_label = Label(ventana, image=img_tk) #colocamos un lable que nos de la imagen. 
                imagen_label.image = img_tk #mostramos la imagen en la ventana con tkner 
                imagen_label.pack()
                ventana.update_idletasks()
                y = (lbl_resultado.winfo_reqheight()  + imagen_label.winfo_reqheight()) +210
                imagen_label.place(x=50,y=y)
                llamadaDatos.imagen_label = imagen_label
    except:
        print("error")
ventana=Tk()
ventana.title('Verificador de Precios')
ventana['bg']='#DE2E03'
ventana.state('zoomed')
#labels
label_codigo = Label(ventana,text="Codigo Del Producto",font = "BOLD")
label_codigo.pack(pady=20)

lbl_resultado=Label(ventana,text="Productos:",font = "Helvetica 16 bold italic")
lbl_resultado.pack(pady=20)


ventana.bind('<Key>', key_pressed)
ventana.mainloop()