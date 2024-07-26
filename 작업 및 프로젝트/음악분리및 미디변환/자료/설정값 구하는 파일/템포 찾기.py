import librosa
import numpy as np
def find_tempo(audio_path):
    # 오디오 위치
    y, sr = librosa.load(audio_path)
    # 오디오 신호 y , 샘플 속도 sr
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


audio_path = 'C:/Users/moon/Downloads/path/음악분리및미디/demucs-main/separated/htdemucs/춘래불사춘/other.wav'
tempo_int, beat_times_int = find_tempo(audio_path)

print(f"템포: {tempo_int} BPM")
print("시간:", beat_times_int) 

#%%
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# 오디오 파일 로드
y, sr = librosa.load('C:/Users/moon/Downloads/path/음악분리및미디/demucs-main/separated/htdemucs/춘래불사춘/other.wav')

# 템포(tempo)와 비트 시간 계산
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 비트 프레임을 시간으로 변환
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# 템포가 배열일 경우 첫 번째 요소를 사용
if isinstance(tempo, np.ndarray):
    tempo = tempo[0]
# 템포를 정수로 반올림
tempo_int = int(round(tempo))

# 비트 시간을 정수로 변환
beat_times_int = [int(round(bt)) for bt in beat_times]

# 결과 출력
print(f"템포: {tempo_int} BPM")
print("시간:", beat_times_int)

# 비트 시간 간격 계산
beat_intervals = [beat_times_int[i+1] - beat_times_int[i] for i in range(len(beat_times_int)-1)]

# 비트 시간과 간격 시각화
plt.figure(figsize=(10, 5))
plt.plot(beat_times_int[:-1], beat_intervals, 'o-')
plt.xlabel('Time (seconds)')
plt.ylabel('Interval (seconds)')
plt.title('Beat Intervals Over Time')
plt.grid(True)
plt.show()