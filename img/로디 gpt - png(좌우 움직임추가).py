import tkinter as tk
import webbrowser

class ClsPersonaje():
    def __init__(self):
        self.pofiFrente = "강아지.png"  # PNG 이미지 경로
        self.contador = 0
        self.direction = 1  # 이동 방향 (1은 오른쪽, -1은 왼쪽)
        self.dx = 5  # 이동 속도

    def fntPersonaje(self, ventana):
        self.ventana = ventana
        self.pofiEnImage = tk.PhotoImage(file=self.pofiFrente)  # PNG 이미지를 PhotoImage로 읽기
        self.pofiEnLabel = tk.Label(ventana, image=self.pofiEnImage)
        self.pofiEnLabel.pack()

        self.pofiEnLabel.bind("<Button-1>", self.on_click)
        self.pofiEnLabel.bind("<B1-Motion>", self.on_drag)

        # 애니메이션 시작
        self.animate()

    def on_click(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def on_drag(self, event):
        x = self.pofiEnLabel.winfo_x() + event.x - self.offset_x
        y = self.pofiEnLabel.winfo_y() + event.y - self.offset_y
        self.pofiEnLabel.place(x=x, y=y)

    def animate(self):
        x = self.pofiEnLabel.winfo_x()
        # 경계 조건 처리 (좌우로 이동)
        if x >= self.ventana.winfo_width() - self.pofiEnImage.width() or x <= 0:
            self.direction *= -1  # 방향 반전

        x += self.dx * self.direction
        self.pofiEnLabel.place(x=x, y=self.pofiEnLabel.winfo_y())

        # 일정 시간 후에 다시 animate 호출
        self.ventana.after(50, self.animate)  # 50 밀리초마다 호출

class ClsVentana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.altoVentana = 1080  # y
        self.anchoVentana = 1920  # x

    def fntParametrosVentana(self, altoVentana, anchoVentana, coordenadaX, coordenadaY):
        self.ventana.geometry(f"{altoVentana}x{anchoVentana}+{coordenadaX}+{coordenadaY}")
        self.ventana.tk_setPalette("beige")
        self.ventana.wm_overrideredirect(True)
        self.ventana.wm_attributes("-topmost", False)  # True 다른 모든 창 위에 표시
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
