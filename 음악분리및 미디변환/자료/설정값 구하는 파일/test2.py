from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

model_output, midi_data, note_events = predict("other.mp3")
'''시작 시간(float): 음표의 시작 시간(초)입니다.
   종료 시간(float): 메모의 오프셋 시간(초)입니다.
   피치(int): 음표의 MIDI 피치 번호입니다.
   신뢰도(float): 메모 감지의 신뢰도 수준입니다.
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
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import predict_and_save
model = ICASSP_2022_MODEL_PATH
input_audio_paths = ['C:/Users/moon/Downloads/path/음악분리및미디/demucs-main/separated/htdemucs/춘래불사춘/bass.wav']
output_directory = 'C:/Users/moon/Downloads/path/음악분리및미디/demucs-main/separated/htdemucs/춘래불사춘'
# C:\Users\moon\Downloads\path\basic-pitch-main\춘래불사춘
predict_and_save(
    input_audio_paths,
    output_directory,
    save_midi=True,
    sonify_midi=False,
    save_model_outputs=True,
    onset_threshold = float(20),  # 0 ~ 100
    frame_threshold = float(0.2), # 0 ~ 1
    save_notes=False,
    # melodia_trick = True,
    minimum_note_length = float(210), # 밀리초
    minimum_frequency = float(160),
    # multiple_pitch_bends = True,
    midi_tempo= float(120),
    model_or_model_path = model
)
# 매개변수의 이름을 명시하지 않고 넣어서 첫번째 인자에 들어가서 작동 됌
# audio_path_list: input_audio_paths 이런식으로 이름을 명시해서 사용해야되는데 위처럼 생략도 가능
#%%
# 문제
# 피치 쪽에서 너무 빠르게 음을 파악하는거 같다 그래서 쪼개는 것도 많고 
# 바이브레이션같은건 다 끊어버리닌까 심각하다
# 음정을 너무 빨리 끝어서 파악하닌까 길게 끌고 가는 음 시간이 지나면 
# 피치가 바뀌는데 그걸 또 음정으로 파악해서 문제가 크다
'''
노트 유형	음표당 비트	120BPM의 지속 시간(초)
온음(세미브레브)	4	2.0
반음표(최소)	2	1.0
4분음표(크로셰)	1	0.5
8분음표(Quaver)	0.5	0.25
16분 음표(반분음표)	0.25	0.125
30초음표(Demisemiquaver)	0.125	0.0625
64분음표(Hemidemisemiquaver)	0.0625	0.03125'''
