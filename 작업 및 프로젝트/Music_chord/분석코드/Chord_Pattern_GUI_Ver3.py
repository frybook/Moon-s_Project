import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, Scrollbar
from Import_csv import csv_text,csv_text2, extract_roman_numerals, select_song
from chord_progressions import token, target_song, convert_data

# GUI 코드 시작
class ChordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("코드 패턴 분석")

        # 배경 색상 설정
        self.root.configure(bg="#E0EFEA")

        # 폰트와 색상 설정
        self.font = ("Arial", 12)
        self.button_bg = "#81BECE"
        self.button_fg = "#000000"

        # 폰트와 버튼 색상 적용
        self.label = tk.Label(root, text="곡 선택하기:", font=self.font, bg="#E0EFEA")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.select_folder_button = tk.Button(root, text="폴더 선택", command=self.select_folder, font=self.font, bg=self.button_bg, fg=self.button_fg)
        self.select_folder_button.grid(row=1, column=0, columnspan=2, pady=5)

        self.song_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=50, font=self.font)
        self.song_listbox.grid(row=2, column=0, columnspan=2, pady=10)

        self.analyze_button = tk.Button(root, text="분석 하기", command=self.analyze_song, font=self.font, bg=self.button_bg, fg=self.button_fg)
        self.analyze_button.grid(row=3, column=0, columnspan=2, pady=5)

        # 텍스트 위젯들을 배치할 프레임을 만듦
        self.text_frame = tk.Frame(root, bg="#f0f0f0")
        self.text_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # 결과 텍스트 위젯 및 스크롤바
        self.result_text = tk.Text(self.text_frame, height=15, width=80, font=self.font, wrap=tk.WORD)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        self.result_scrollbar = Scrollbar(self.text_frame, command=self.result_text.yview)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=self.result_scrollbar.set)

        # Roman numerals 텍스트 위젯 및 스크롤바
        self.roman_numerals_text = tk.Text(root, height=40, width=40, font=self.font, wrap=tk.WORD)
        self.roman_numerals_text.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

        self.roman_scrollbar = Scrollbar(root, command=self.roman_numerals_text.yview)
        self.roman_scrollbar.grid(row=0, column=3, rowspan=5, sticky='ns')
        self.roman_numerals_text.config(yscrollcommand=self.roman_scrollbar.set)

        # select_song_chords2 텍스트 위젯 및 스크롤바
        self.select_song_chords2_text = tk.Text(root, height=40, width=40, font=self.font, wrap=tk.WORD)
        self.select_song_chords2_text.grid(row=0, column=4, rowspan=5, padx=10, pady=10)

        self.select_song_chords2_scrollbar = Scrollbar(root, command=self.select_song_chords2_text.yview)
        self.select_song_chords2_scrollbar.grid(row=0, column=5, rowspan=5, sticky='ns')
        self.select_song_chords2_text.config(yscrollcommand=self.select_song_chords2_scrollbar.set)

        self.rm_chord_frames = None
        self.Og_chord_frames = None  # Og_chord_frames 초기화
        self.song_list = []

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            # 실제 데이터 로드
            self.rm_chord_frames = csv_text()  # 이 함수에서 데이터를 로드하도록 수정
            self.Og_chord_frames = csv_text2()  # 이 함수에서 데이터를 로드하도록 수정
            self.song_list = list(self.rm_chord_frames.keys())
            self.update_song_listbox()

    def update_song_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for song in self.song_list:
            self.song_listbox.insert(tk.END, song)

    def analyze_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            index_position = selected_index[0]  # 선택된 인덱스를 가져옴
            select_song_chords = select_song(self.rm_chord_frames, index_position)
            select_song_chords2 = select_song(self.Og_chord_frames, index_position)  # select_song_chords2 추가
            roman_numerals = extract_roman_numerals(select_song_chords)
            tokenized_progressions, tokenized_roman = token(roman_numerals)
            token_pattern = target_song(tokenized_progressions, tokenized_roman)
            chords_pattern = convert_data(token_pattern)
            self.display_roman_numerals(roman_numerals)
            self.display_results(chords_pattern)
            self.display_select_song_chords2(select_song_chords2)  # select_song_chords2 표시
        else:
            messagebox.showwarning("찾지 못했습니다.", "목록에서 곡을 선택하세요")

    def display_roman_numerals(self, roman_numerals):
        self.roman_numerals_text.delete(1.0, tk.END)
        for numeral in roman_numerals:
            self.roman_numerals_text.insert(tk.END, f"{numeral}\n")

    def display_results(self, chords_pattern):
        self.result_text.delete(1.0, tk.END)
        if not chords_pattern:
            self.result_text.insert(tk.END, "비슷한 유형을 찾지 못했습니다.")
        for i, item in enumerate(chords_pattern):
            chord_progression, best_match, ratio = item
            self.result_text.insert(tk.END, f"패턴 {i + 1}:\n")
            self.result_text.insert(tk.END, f"  코드 진행 유형: {chord_progression}\n")
            self.result_text.insert(tk.END, f"  곡 정보: {best_match}\n")
            self.result_text.insert(tk.END, f"  유사도: {ratio:.2f}\n")
            self.result_text.insert(tk.END, "-----------------------\n")

    def display_select_song_chords2(self, select_song_chords2):
        self.select_song_chords2_text.delete(1.0, tk.END)
        for chord in select_song_chords2:
            self.select_song_chords2_text.insert(tk.END, f"{chord}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChordApp(root)
    root.mainloop()