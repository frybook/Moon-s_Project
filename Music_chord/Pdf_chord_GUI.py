import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics, export_to_csv
from line_filter import line_filter

# 실행
def analyze_file():
    try:
        # PDF파일 위치
        pdf_file_path = file_path.get()
        
        # PDF 가공
        lines, key_name, title = text_setting(pdf_file_path)
        cleaned_lines = text_chords(lines)
        text_separation, change_indices, Order_of_keys = line_filter(cleaned_lines)
        chords = Find_chords(text_separation)  # 코드 악보
        Roman_chords_list, original_chords_list = harmonics(Order_of_keys, chords)  # 로마 악보
        
        # 내보낼 위치
        export_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
                                                  initialfile=f"{title}")
        
        # CSV파일 결과
        export_to_csv(Roman_chords_list, original_chords_list, key_name, title, export_path)
        
        messagebox.showinfo("Success", "분석이 완료되었으며 결과가 CSV로 내보내졌습니다.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# PDF파일 위치 설정
def select_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

# GUI 설정
root = tk.Tk()
root.title("PDF에서 코드 추출")

file_path = tk.StringVar()

# GUI 옵션
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="선택", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="추출", command=analyze_file).grid(row=1, column=1, pady=10)

# GUI 실행
root.mainloop()


#%%
'''
업데이트 한내용
자동으로 key 찾아주기(수리중)
전조곡들의 여부
제외 단어 쉽게 코드화
코드 분리화 수정
전조되는 부분을 나눠서 키와 코드를 분리
original과 roman 를 csv로 저장해서 데이터 수집
구간을 설정해서 제목및 작곡가 같은 텍스트화에 불필요한 정보 제외
'''
