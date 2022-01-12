import wave as wave
import sounddevice as sd
import numpy as np

wave_length=5
sample_rate=44100

print("録音開始")

data=sd.rec(int(wave_length*sample_rate), sample_rate, channels=2)
sd.wait()

print("録音終了")

# wavファイルに書き込み
wave_out=wave.open("./wgn_wave.wav", 'w')

# モノラル:1、ステレオ:2
wave_out.setnchannels(2)

# サンプルサイズ設定（2バイト）
wave_out.setsampwidth(2)

# サンプリング周波数
wave_out.setframerate(sample_rate)

# データを書き込み
wave_out.writeframes(data)

# ファイルを閉じる
wave_out.close()
