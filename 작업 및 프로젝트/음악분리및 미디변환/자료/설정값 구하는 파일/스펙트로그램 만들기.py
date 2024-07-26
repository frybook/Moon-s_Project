import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# 오디오 파일 로드
y, sr = librosa.load('vocals.wav')

# 스펙트로그램 계산
S = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

# 스펙트로그램 그리기
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()