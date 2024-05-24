import aubio
import numpy as np
from midiutil import MIDIFile


audio_path = 'C:/Users/moon/Downloads/path/음악분리및미디/demucs-main/separated/htdemucs/춘래불사춘/other.wav'

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





