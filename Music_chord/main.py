from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import extract_base_note,extract_chord_type,harmonics

if __name__ == "__main__":
    lines = text_setting()
    cleaned_lines = text_chords(lines)
    chords = Find_chords(cleaned_lines)
    Transformation_roman = harmonics(chords)
    print("추출된 코드(악보 기호):")
    for chord in chords:
        print(chord)
    for roman in Transformation_roman:
        print(roman)


#%%
"""
업데이트 해야 할 내용:    
    제외할 단어 문장을 여러개 지정 가능하게 설정
    영어 가사의 대한 근본적인 문제를 해결(결국 위에도 같은 내용)
    Major or minor 따라 바뀌는 스케일
    변조곡들은 어떻게 설정할지
    dual funtion은 어떻게 할것인가?
"""

#%%

'''
코드 진행 :
    4도 - 3도7 - 6도 : 슬프고 어두운 느낌
    2도 - 5도  - 1도 : 근본
    
    
    '''