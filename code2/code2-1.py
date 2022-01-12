import wave as wave
import pyroomacoustics as pa
import numpy as np

# カーネギーメロン大学 言語技術研究所 ARCTIC コーパス
pa.datasets.CMUArcticCorpus(basedir="./CMU_ARCTIC", download=True,speaker=["aew", "axb"])
sample_wave_file="./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"

# サンプルwavファイルを開く
wav=wave.open(sample_wave_file)

# 属性を表示
print("サンプリング周波数[Hz]: ", wav.getframerate())
print("サンプルサイズ[Bytes]: ", wav.getsampwidth())
print("サンプル数: ", wav.getnframes())
print("チャネル数: ", wav.getnchannels())

# 音声データを展開
data=wav.readframes(wav.getnframes())
data=np.frombuffer(data, dtype=np.int16)

wav.close()
