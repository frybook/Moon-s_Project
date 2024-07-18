import tkinter as tk
from tkinter import filedialog, messagebox
from Import_csv import csv_text,extract_roman_numerals,select_song
from chord_progressions import token,target_song,convert_data

# GUI 코드 시작
class ChordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("코드 패턴 분석")

        self.label = tk.Label(root, text="곡 선택하기:")
        self.label.pack(pady=10)

        self.select_folder_button = tk.Button(root, text="폴더 선택", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

        self.song_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=50)
        self.song_listbox.pack(pady=10)

        self.analyze_button = tk.Button(root, text="분석 하기", command=self.analyze_song)
        self.analyze_button.pack(pady=5)

        self.result_text = tk.Text(root, height=20, width=80)
        self.result_text.pack(pady=10)

        self.rm_chord_frames = None
        self.song_list = []

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            # 실제 데이터 로드
            self.rm_chord_frames = csv_text()  # 이 함수에서 데이터를 로드하도록 수정
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
            roman_numerals = extract_roman_numerals(select_song_chords)
            tokenized_progressions, tokenized_roman = token(roman_numerals)
            token_pattern = target_song(tokenized_progressions, tokenized_roman)
            chords_pattern = convert_data(token_pattern)
            self.display_results(chords_pattern)
        else:
            messagebox.showwarning("찾지 못했습니다.", "목록에서 곡을 선택하세요")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = ChordApp(root)
    root.mainloop()
    
#%%
"""
선택 했을 경우 패턴이 없는경우 유사한 패턴을 찾지못하였습니다.


"""

