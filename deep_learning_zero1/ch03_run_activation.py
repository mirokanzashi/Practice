
import numpy as np
import matplotlib.pylab as plt
import lib.activation_func as func

"""
config共通化
configを関数内で自動展開
pltの設定追加（フォント、タイトルなど）
x=0 の垂直線を追加
複数ウィンドウを立ち上がる
"""
class PlotConfig:
    def __init__(self, window_title="Figure", figure_title="", linestyle="--", ylim=(-0.1,1.1)):
        self.window_title = window_title
        self.figure_title = figure_title
        self.linestyle = linestyle
        self.ylim = ylim

def _window_config(**kwargs):
    config = {**kwargs}
    fig = plt.figure()
    fig.canvas.manager.set_window_title(config["window_title"])
    
    
    # plt.axhline(0, color='gray', linestyle='--')  # y=0 の水平線
    plt.axvline(0, color='gray', linestyle='--')  # x=0 の垂直線
    # plt.grid(color='gray', linestyle='--', linewidth=0.5)


    plt.ylim(config["ylim"])  # 図で描画するy軸の範囲を指定
    plt.rcParams['font.family'] = 'Meiryo' # フォント設定
    plt.title(config["figure_title"])

def window_draw(x, y, **kwargs):

    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("x と y は NumPy 配列である必要があります")
    # 空チェック
    if x.size == 0 or y.size == 0:
        raise ValueError("x または y が空です")
    # window_block=kwargs.get("window_block",True)
    _window_config(**kwargs)
    plt.plot(X, Y)
    

def window_show(**kwargs):
    plt.show(block=kwargs.get("window_block",True))

if __name__ == '__main__':
    X = np.arange(-5.0, 5.0, 0.1)

    Y = func.sigmoid_func(X)
    sigmoid_config = PlotConfig(window_title="シグモイド関数", figure_title="sigmoid")
    window_draw(X,Y,**sigmoid_config.__dict__ )

    Y = func.step_func(X)
    step_config = PlotConfig(window_title="ステップ関数", figure_title="step")
    window_draw(X,Y,**step_config.__dict__ )

    Y = func.relu_func(X)
    relu_config = PlotConfig(window_title="ReLu関数", figure_title="relu",ylim=(-1.0,5.5))
    window_draw(X,Y,**relu_config.__dict__ )
    
    window_show(window_block=True)
    pass