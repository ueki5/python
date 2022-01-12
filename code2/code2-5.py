import wave as wave
import sounddevice as sd
import numpy as np

# サンプルwavファイルを開く
#sample_wave_file="./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
#sample_wave_file="./wgn_wave.wav"
sample_wave_file="./recording.wav"
wav=wave.open(sample_wave_file)

# 属性を表示
print("サンプリング周波数[Hz]: ", wav.getframerate())
print("サンプルサイズ[Bytes]: ", wav.getsampwidth())
print("サンプル数: ", wav.getnframes())
print("チャネル数: ", wav.getnchannels())

# 音声データを展開
data=wav.readframes(wav.getnframes())
data=np.frombuffer(data, dtype=np.int16)
# 音声データを再生
sd.play(data, wav.getframerate())

print("再生開始")

status=sd.wait()

wav.close()
