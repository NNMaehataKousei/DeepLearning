import sys, os
import numpy as np

sys.path.append(os.pardir)
from dqn_lesson7.util import im2col

"""
x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)

x2 = np.random.rand(10, 3, 7, 7) #10個のデータ
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape)
"""
class Convolutuon:
    def __init__(self, W, b, stride=1,  pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2*self.pad - FH)/self.stride)
        out_w = int(1 + (W + 2*self.pad - FW)/self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T
        out = np.dot(col, col_W) + self.b

        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out

"""
初期化メソッドはフィルター(重み)とバイアス、ストライドとパディングを引数として受け取り、フィルターは4次元の形状である。
"""
#poolingレイヤもim2colを使って実装

class pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        N, C, H, W  = x.shape
        out_h = ini(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)
        
        #展開

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h*self.pool_w)

        #最大値(2)
        out = np.max(col, axis=1)
        #整形
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        return out

