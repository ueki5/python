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
data=np.random.normal(loc=0.0, scale=0.1, size=4)
