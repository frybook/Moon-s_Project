import tkinter as tk

class ClsPersonaje():
    def __init__(self):
        self.pofiFrente = "강아지.png"  # PNG 이미지 경로
        self.contador = 0
        self.is_dragging = False

    def fntPersonaje(self, ventana):
        self.ventana = ventana
        self.pofiEnImage = tk.PhotoImage(file=self.pofiFrente)  # PNG 이미지를 PhotoImage로 읽기
        self.pofiEnLabel = tk.Label(ventana, image=self.pofiEnImage)
        self.pofiEnLabel.pack()

        self.pofiEnLabel.bind("<Button-1>", self.on_click)
        self.pofiEnLabel.bind("<B1-Motion>", self.on_drag)

    def on_click(self, event):
        self.is_dragging = True
        self.offset_x = event.x
        self.offset_y = event.y

    def on_drag(self, event):
        if self.is_dragging:
            x = self.pofiEnLabel.winfo_x() + event.x - self.offset_x
            y = self.pofiEnLabel.winfo_y() + event.y - self.offset_y
            self.pofiEnLabel.place(x=x, y=y)

import webbrowser

class ClsVentana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.altoVentana = 1080   # y
        self.anchoVentana = 1920   # x

    def fntParametrosVentana(self, altoVentana, anchoVentana, coordenadaX, coordenadaY):
        self.ventana.geometry(f"{altoVentana}x{anchoVentana}+{coordenadaX}+{coordenadaY}")
        self.ventana.tk_setPalette("beige")
        self.ventana.wm_overrideredirect(True)
        self.ventana.wm_attributes("-topmost", False) # True 다른 모든 창 위에 표시
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