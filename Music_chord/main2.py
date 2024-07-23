from Import_csv import csv_text,csv_text2,extract_roman_numerals,select_songs
from chord_progressions import token,target_song,convert_data
import pandas as pd
# from Import_csv import *

#%%


#%%

if __name__ == "__main__":
    folder_path = "C:\Python\Syntex\working\개인\악보\분석"
    Rm_chord_frames = csv_text(folder_path)
    Og_chord_frames = csv_text2(folder_path)
    song_list = list(Rm_chord_frames.keys())
    song_list2 = list(Og_chord_frames.keys())
    select_song_chords,select_song_chords2 = select_songs(Rm_chord_frames,song_list,Og_chord_frames,song_list2)
    roman_numerals = extract_roman_numerals(select_song_chords)
    tokenized_progressions,tokenized_roman = token(roman_numerals)
    token_pattern = target_song(tokenized_progressions,tokenized_roman)
    chords_pattern = convert_data(token_pattern)
    for i, item in enumerate(chords_pattern):
        chord_progression, best_match, ratio = item
        print(f"데이터 {i + 1}:")
        print(f"  코드 패턴: {chord_progression}")
        print(f"  곡에서 진행: {best_match}")
        print(f"  정확도: {ratio:.2f}")
        print('---')
#%%

print(roman_numerals)
