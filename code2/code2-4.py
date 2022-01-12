import wave as wave
import pyroomacoustics as pa
import numpy as np

# 白色雑音を生成する
n_sample=4000
sample_rate=16000

# 乱数の種を設定
np.random.seed(0)

# 白色雑音を生成
#data=np.random.normal(scale=0.1, size=n_sample)
#data=np.random.normal(scale=1, size=4)
data=np.random.normal(loc=0.0, scale=0.1, size=n_sample)

# 16ビットのデータとして書き込む為、スケールを調整して型変換
data_scale_adjust=(data*np.iinfo(np.int16).max).astype(np.int16)

# wavファイルに書き込み
wave_out=wave.open("./wgn_wave.wav", 'w')

# モノラル:1、ステレオ:2
wave_out.setnchannels(1)

# サンプルサイズ設定（2バイト）
wave_out.setsampwidth(2)

# サンプリング周波数
wave_out.setframerate(sample_rate)

# データを書き込み
wave_out.writeframes(data_scale_adjust)

# ファイルを閉じる
wave_out.close()
