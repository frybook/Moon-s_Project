
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save
model = ICASSP_2022_MODEL_PATH
input_audio_paths = ['음원 위치']
output_directory = '디렉토리 위치'
predict_and_save(
    input_audio_paths,                # 오디오 위치
    output_directory,                 # 출력할 디렉토리 위치
    save_midi=True,                   # 미디 출력 여부
    sonify_midi=False,                # 미디를 오디오 파일 출력 여부
    save_model_outputs=True,          # 모델에 참고사항
    onset_threshold = float(80),      # 시작이 존재하는 것으로 간주되는 데 필요한 최소 에너지 0 ~ 100까지
    frame_threshold = float(0.25),    # 프레임이 존재하는 것으로 간주되기 위한 최소 에너지 0 ~ 1 까지
    save_notes=True,                  # save_notes 정보를 csv 파일 출력 여부
    melodia_trick = True,             # 후처리 단계는 추출된 멜로디 데이터를 더 유의미하고 유용 만드는 역할
    minimum_note_length = float(200), # 허용되는 최소 노트 길이(밀리초)
    minimum_frequency = float(160),   # 허용되는 최소 출력 주파수(Hz)
    multiple_pitch_bends = True,      # 미디 파일의 겹치는 음표에 피치 벤드가 있도록 허용
    midi_tempo= float(120),           # 템포
    model_or_model_path = model       # 모델
)

#%%
# note_events 확인
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

model_output, midi_data, note_events = predict("other.wav")
'''시작 시간(float): 음표의 시작 시간(초)입니다.
   종료 시간(float): 메모의 오프셋 시간(초)입니다.
   pitch(int): 음표의 MIDI 피치 번호입니다.
   velocity(float): 메모 감지의 신뢰도 수준입니다.
   Optional[List[int]]: 피치 벤드 목록(인 경우 include_pitch_bends) True.
   0-12: C0 ~ B0(매우 낮은 피치)
   13-24: C1 ~ B1(낮은 음조)
   25-36: C2 ~ B2(중간 피치)
   37-48: C3 ~ B3(높은 음조)
   49-60: C4 ~ B4(고음)
   61-72: C5 ~ B5(매우 높은 음조)
   73-84: C6 ~ B6(매우 높은 음조)
   85-96: C7 ~ B7(매우 높은 음조)
   97-108: C8 ~ B8(매우 높은 음조)
   109-120: C9 ~ B9(매우 높은 음조)
   121-127: C10 ~ B10(매우 높은 피치)'''

#%%
# 피치 확인과 시간
import aubio


audio_path = '음원 위치'

# 샘플링 속도 및 기타 매개변수 설정
samplerate = 44100  # 오디오 파일의 샘플링 속도
win_s = 1024  # FFT 
hop_s = win_s // 2  # Hop 

# 오디오 파일을 읽기 위한 소스 객체 생성
source = aubio.source(audio_path, samplerate, hop_s)

# 피치 감지 개체
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("Hz")
pitch_o.set_silence(-40)

total_frames = 0
pitches = []
times = []

while True:
    samples, read = source()
    pitch = pitch_o(samples)[0]
    pitches.append(pitch)
    times.append(total_frames / float(samplerate))
    total_frames += read
    if read < hop_s:
        break

#%%
# 템포 및 비트 프레임
import librosa
import numpy as np
def find_tempo(audio_path):
    # 오디오 위치
    y, sr = librosa.load(audio_path)
    
    # 템포 및 비트 프레임
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    # 비트 프레임을 시간으로 변환
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    if isinstance(tempo, np.ndarray):
        tempo = tempo[0]
    # 템포를 정수로 반올림
    tempo_int = int(round(tempo))
    # 비트 시간을 정수로 변환
    beat_times_int = [int(round(bt)) for bt in beat_times]
    
    return tempo_int, beat_times_int


audio_path = '오디오위치'
tempo_int, beat_times_int = find_tempo(audio_path)

print(f"템포: {tempo_int} BPM")
print("시간:", beat_times_int) 

#%%
# 120 BPM 기준 음표에 시간
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
