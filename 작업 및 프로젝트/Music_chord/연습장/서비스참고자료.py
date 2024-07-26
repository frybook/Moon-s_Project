# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:03:26 2024

@author: YS702
"""

import tkinter as tk
from tkinter import messagebox

# 함수: 입력 데이터 가져오기
def get_input():
    age = entry_age.get()
    budget = entry_budget.get()
    family_members = entry_family_members.get()
    
    selected_infra = []
    for var, label in zip(infra_vars, infra_labels):
        if var.get():
            selected_infra.append(label)
    
    messagebox.showinfo("입력 정보", f"나이: {age}\n예산: {budget}\n가족 구성원 수: {family_members}\n선호 인프라: {', '.join(selected_infra)}")

# 함수: 상태창 업데이트
def update_status():
    age = entry_age.get()
    budget = entry_budget.get()
    family_members = entry_family_members.get()
    
    selected_infra = []
    for var, label in zip(infra_vars, infra_labels):
        if var.get():
            selected_infra.append(label)
    
    status_text.set(f"나이: {age}\n예산: {budget}\n가족 구성원 수: {family_members}\n선호 인프라: {', '.join(selected_infra)}")

# GUI 생성
root = tk.Tk()
root.title("댑트동산")

# 입력 프레임 생성
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# 상태 프레임 생성
status_frame = tk.Frame(root)
status_frame.grid(row=0, column=1, padx=10, pady=10)

# 나이 입력
tk.Label(input_frame, text="나이:").grid(row=0, column=0)
entry_age = tk.Entry(input_frame)
entry_age.grid(row=0, column=1)
entry_age.bind("<KeyRelease>", lambda event: update_status())

# 예산 입력
tk.Label(input_frame, text="예산:").grid(row=1, column=0)
entry_budget = tk.Entry(input_frame)
entry_budget.grid(row=1, column=1)
entry_budget.bind("<KeyRelease>", lambda event: update_status())

# 가족 구성원 수 입력
tk.Label(input_frame, text="가족 구성원 수:").grid(row=2, column=0)
entry_family_members = tk.Entry(input_frame)
entry_family_members.grid(row=2, column=1)
entry_family_members.bind("<KeyRelease>", lambda event: update_status())

# 선호 인프라 입력
tk.Label(input_frame, text="선호 인프라:").grid(row=3, column=0, columnspan=2)
infra_labels = ["지하철", "초등학교", "중학교", "고등학교", "종합병원", "대형마트", "대형공원"]
infra_vars = [tk.IntVar() for _ in infra_labels]

for i, label in enumerate(infra_labels):
    chk = tk.Checkbutton(input_frame, text=label, variable=infra_vars[i], command=update_status)
    chk.grid(row=4+i, column=0, columnspan=2, sticky='w')

# 제출 버튼
submit_button = tk.Button(input_frame, text="제출", command=get_input)
submit_button.grid(row=11, column=0, columnspan=2)

# 상태창 라벨 생성
status_text = tk.StringVar()
status_label = tk.Label(status_frame, textvariable=status_text, justify='left', anchor='w')
status_label.grid(row=0, column=0)

# 초기 상태 업데이트
update_status()

# GUI 실행
root.mainloop()