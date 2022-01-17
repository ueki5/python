import wave as wave
import sounddevice as sd
import numpy as np

wave_length=5 # 単位（秒）
sample_rate=44100
sample_size=2
channels=2

print("録音開始")

data=sd.rec(int(wave_length*sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
sd.wait()

print("録音終了")

# wavファイルに書き込み
wave_out=wave.open("./wgn_wave.wav", 'w')

# モノラル:1、ステレオ:2
wave_out.setnchannels(channels)

# サンプルサイズ設定
wave_out.setsampwidth(sample_size)

# サンプリング周波数
wave_out.setframerate(sample_rate)

# フレーム数を設定
wave_out.setnframes(wave_length*sample_rate)

# データを書き込み
wave_out.writeframes(data)

# ファイルを閉じる
wave_out.close()
