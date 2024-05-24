
import pandas as pd


data = {
    '음표': ['온음', '2분음표', '4분음표', '8분음표','16분음표','32분음표','64분음표'],
    '박자': [4, 2, 1, 0.5, 0.25, 0.125, 0.0625]
}


df = pd.DataFrame(data)
df.set_index('음표', inplace=True)

# BPM 값에 따라 각 노트 유형의 지속 시간을 계산하는 함수 정의
def calculate_durations(bpm):
    # 한 비트의 지속 시간을 초 단위로 계산
    beat_duration = 60 / bpm
    # 각 노트 유형의 지속 시간 계산
    df['지속시간(초)'] = df['박자'] * beat_duration
    return df

# 최대 64분 음표까지의 모든 음 유형으로 코드를 생성하는 기능을 정의
def generate_chord(bpm):
    chord_df = calculate_durations(bpm)
    return chord_df


bpm = 120
chord_df = generate_chord(bpm)
print(chord_df)