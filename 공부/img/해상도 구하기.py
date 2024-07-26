
import tkinter as tk

root = tk.Tk()

# 데스크톱 화면의 가로 및 세로 해상도 가져오기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("데스크톱 화면의 가로 해상도:", screen_width)
print("데스크톱 화면의 세로 해상도:", screen_height)
