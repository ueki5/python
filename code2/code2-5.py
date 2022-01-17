import wave as wave
import sounddevice as sd
import numpy as np

# サンプルwavファイルを開く
#sample_wave_file="./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
sample_wave_file="./wgn_wave.wav"
#sample_wave_file="./recording.wav"
wav=wave.open(sample_wave_file)

# 属性を表示
frame_rate=wav.getframerate()
sample_size=wav.getsampwidth()
frame_count=wav.getnframes()
channels=wav.getnchannels()
print("サンプリング周波数[Hz]: ", frame_rate)
print("サンプルサイズ[Bytes]: ", sample_size)
print("サンプル数: ", frame_count)
print("チャネル数: ", channels)

# 音声データを展開
data=wav.readframes(wav.getnframes())
data=np.frombuffer(data, dtype=np.int16)

# ステレオの場合、２次元配列に変換
if channels==2:
    data=data.reshape(frame_count, channels)
# 音声データを再生
sd.play(data, frame_rate)

print("再生開始")

status=sd.wait()

wav.close()
