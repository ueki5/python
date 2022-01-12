import wave as wave
import numpy as np
import matplotlib.pyplot as plt

# サンプルwavファイルを開く
#sample_wave_file="./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
sample_wave_file="./wgn_wave.wav"
wav=wave.open(sample_wave_file)

# 音声データを展開
data=wav.readframes(wav.getnframes())
data=np.frombuffer(data, dtype=np.int16)

wav.close()

# 音声の大きさ（y軸）を正規化(-1 ～ 1)
#y=data
y=data/np.iinfo(np.int16).max
# 時間軸（x軸）の設定 [0, 1/16000, 2/16000 … 62080/16000]
x=np.array(range(wav.getnframes()))/wav.getframerate()

plt.figure(figsize=(10, 4))
plt.xlabel("Time [sec]")
plt.ylabel("Value [-1, 1]")
plt.plot(x, y)
plt.savefig("./wave_form.png")
plt.show()
