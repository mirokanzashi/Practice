
from graphviz import Digraph
import lib.activation_func as func
import numpy as np
# forward計算して各層の活性化値を返す
def forward_trace(Ws, bs, x):
    W1,W2,W3 = Ws
    b1,b2,b3 = bs

    a1 = np.dot(x, W1) + b1
    z1 = func.sigmoid_func(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = func.sigmoid_func(a2)

    a3 = np.dot(z2, W3) + b3
    y = a3  # identity

    return {
        'x': x,
        'z1': z1,
        'z2': z2,
        'y': y
    }
def draw_nn():
    Ws, bs = init_network()
    x = np.array([1.0, 0.5])
    trace = forward_trace(Ws, bs, x)

    dot = Digraph(comment='NN Grapth', format='png')
    dot.attr(rankdir='LR', size='10')  # 左から右へ

    # バイアスノード
    with dot.subgraph() as s:
        s.attr(rank='same')
        for l, b_layer in enumerate(bs):
            for i, val in enumerate(b_layer):
                s.node(f'b{l+1}_{i+1}', f'b{l+1}_{i+1}\nval={val:.5f}', style='filled', fillcolor='lightyellow')

    # 入力層
    with dot.subgraph() as s:
        s.attr(rank='same')
        for i, val in enumerate(trace['x']):
            s.node(f'x{i+1}', f'x{i+1}\nval={val:.5f}', style='filled', fillcolor='lightblue')

    # 隠れ層1
    with dot.subgraph() as s:
        s.attr(rank='same')
        for i, val in enumerate(trace['z1']):
            s.node(f'h1{i+1}', f'h1_{i+1}\nval={val:.5f}', style='filled', fillcolor='lightgreen')

    # 隠れ層2
    with dot.subgraph() as s:
        s.attr(rank='same')
        for i, val in enumerate(trace['z2']):
            s.node(f'h2{i+1}', f'h2_{i+1}\nval={val:.5f}', style='filled', fillcolor='lightgreen')

    # 出力層
    with dot.subgraph() as s:
        s.attr(rank='same')
        for i, val in enumerate(trace['y']):
            s.node(f'y{i+1}', f'y{i+1}\nval={val:.5f}', style='filled', fillcolor='lightpink')

    # 入力層 → 隠れ層1
    for i, x_name in enumerate(['x1','x2']):
        for j, h_name in enumerate(['h11','h12','h13']):
            dot.edge(x_name, h_name, label=f'W={Ws[0][i,j]}')
    # バイアス1 → 隠れ層1
    for i in range(3):
        dot.edge(f'b1_{i+1}', f'h1{i+1}', label=f'b={bs[0][i]}')

    # 隠れ層1 → 隠れ層2
    for i, h1_name in enumerate(['h11','h12','h13']):
        for j, h2_name in enumerate(['h21','h22']):
            dot.edge(h1_name, h2_name, label=f'W={Ws[1][i,j]}')
    # バイアス2 → 隠れ層2
    for i in range(2):
        dot.edge(f'b2_{i+1}', f'h2{i+1}', label=f'b={bs[1][i]}')

    # 隠れ層2 → 出力層
    for i, h2_name in enumerate(['h21','h22']):
        for j, y_name in enumerate(['y1','y2']):
            dot.edge(h2_name, y_name, label=f'W={Ws[2][i,j]}')
    # バイアス3 → 出力層
    for i in range(2):
        dot.edge(f'b3_{i+1}', f'y{i+1}', label=f'b={bs[2][i]}')

    dot.render('nn_graph', view=True)


def init_network():
    network_W=[
        np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]),
        np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]]),
        np.array([[0.1,0.3],[0.2,0.4]])
    ]
    network_b=[
        np.array([0.1,0.2,0.3]),
        np.array([0.1,0.2]),
        np.array([0.1,0.2])
    ]
    return network_W,network_b
def identity_function(x):
    return x

def forward(Ws,bs,x):
    W1,W2,W3=Ws[0],Ws[1],Ws[2]
    b1,b2,b3=bs[0],bs[1],bs[2]

    a1=np.dot(x,W1)+b1
    z1=func.sigmoid_func(a1)
    a2=np.dot(z1,W2)+b2
    z2=func.sigmoid_func(a2)
    a3=np.dot(z2,W3)+b3
    y= identity_function(a3)
    return y

def run():
    # 入力
    x = np.array([1.0, 0.5])
    # 重み・バイアス
    Ws, bs = init_network()
    
    y=forward(Ws,bs,x)
    print(y)

    # 描画
    draw_nn()
    
if __name__ == '__main__':
    run()
    pass