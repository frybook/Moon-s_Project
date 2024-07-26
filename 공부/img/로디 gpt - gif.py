import tkinter as tk

class ClsPersonaje():
    def __init__(self):
        self.pofiFrente = "강아지.png"
        self.frames = 18
        self.mostrarImagenes = [tk.PhotoImage(file=self.pofiFrente, format=f"gif -index {i}") for i in range(self.frames)]
        self.contador = 0
        self.is_dragging = False

    def fntPersonaje(self, ventana):
        self.ventana = ventana
        self.pofiEnLabel = tk.Label(ventana, image="")
        self.pofiEnLabel.pack()

        self.pofiEnLabel.bind("<Button-1>", self.on_click)
        self.pofiEnLabel.bind("<B1-Motion>", self.on_drag)

        self.fntAnimacion(self.contador, self.mostrarImagenes, self.frames)

    def fntAnimacion(self, contador, mostrarImagenes, frames):
        self.iteradorImagen = mostrarImagenes[contador]
        self.pofiEnLabel.configure(image=self.iteradorImagen)
        contador += 1
        if contador == frames:
            contador = 0
        self.animacion = self.ventana.after(200, lambda: self.fntAnimacion(contador, mostrarImagenes, frames))

    def on_click(self, event):
        self.is_dragging = True
        self.offset_x = event.x
        self.offset_y = event.y

    def on_drag(self, event):
        if self.is_dragging:
            x = self.pofiEnLabel.winfo_x() + event.x - self.offset_x
            y = self.pofiEnLabel.winfo_y() + event.y - self.offset_y
            self.pofiEnLabel.place(x=x, y=y)
            
#%%
import webbrowser

class ClsVentana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.altoVentana = 1000   # y
        self.anchoVentana = 1900   # x

    def fntParametrosVentana(self, altoVentana, anchoVentana, coordenadaX, coordenadaY):
        self.ventana.geometry(f"{altoVentana}x{anchoVentana}+{coordenadaX}+{coordenadaY}")
        self.ventana.tk_setPalette("beige")
        self.ventana.wm_overrideredirect(True)
        self.ventana.wm_attributes("-topmost", True)
        self.ventana.wm_attributes("-transparentcolor", "beige")
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())

        objClsPersonaje = ClsPersonaje()
        objClsPersonaje.fntPersonaje(self.ventana)
        objClsPersonaje.pofiEnLabel.bind("<Double-Button-1>", self.open_website)
        self.ventana.mainloop()

    def fntPosicionInicial(self):
        anchoPantalla = self.ventana.winfo_screenwidth()
        altoPantalla = self.ventana.winfo_screenheight()

        coordernadaX = anchoPantalla - self.anchoVentana
        coordernadaY = altoPantalla - self.altoVentana
        self.fntParametrosVentana(self.anchoVentana, self.altoVentana, coordernadaX, coordernadaY)
   
    def open_website(self, event):
    # 웹사이트 열기
        webbrowser.open("https://chatgpt.com")
if __name__ == '__main__':
    objVentana = ClsVentana()
    objVentana.fntPosicionInicial()
    

#%%

