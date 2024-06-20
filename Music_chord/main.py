from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics

if __name__ == "__main__":
    lines,key_name = text_setting()
    cleaned_lines = text_chords(lines)
    chords = Find_chords(cleaned_lines)      # 코드 악보
    Transformation_roman,Full_Trans = harmonics(chords,key_name) # 로마 악보



#%%
"""
업데이트 해야 할 내용:    
    제외할 단어 문장을 여러개 지정 가능하게 설정
    영어 가사의 대한 근본적인 문제를 해결(결국 위에도 같은 내용)
    Major or minor 따라 바뀌는 스케일
    전조곡들은 어떻게 설정할지(어느정도 해결)
    전조가 있기전에 &나오고 #,b이 몇개가 붙는지 나온다
    dual funtion은 어떻게 할것인가?
    * 근본적인 문제가 영어 가사의 등장,
    * 분석할때 다른키에서 중복된 key의 값이 같을때 전조했을때 그키의 분석으로해야되는데 전조 전에 키로 분석
업데이트 한내용
자동으로 key 찾아주기(수리중)
전조곡들의 여부
제외 단어 쉽게 코드화
"""

#%%

'''
코드 진행 :
    4도 - 3도7 - 6도 : 슬프고 어두운 느낌
    2도 - 5도  - 1도 : 근본
  Boy  
    
    '''

