from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords


if __name__ == "__main__":
    lines = text_setting()
    cleaned_lines = text_chords(lines)
    chords = Find_chords(cleaned_lines)
    print("추출된 코드(악보 기호):")
    for chord in chords:
        print(chord)


"""
제외할 단어 문장을 여러개 지정 가능하게 설정
영어 가사의 대한 근본적인 문제를 해결(결국 위에도 같은 내용)
"""
#%%
