import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle
import lib.activation_func as active_func

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def run_mnist():
    """
    MNISTの1枚目の画像を表示する
    """
    (x_train, t_train), (_, _) = load_mnist(flatten=True, normalize=False)

    img = x_train[0]
    label = t_train[0]
    print(label)  # 5
    # img_show(img) # ここで画像表示のコードを追加すると、flattenの元データが見える
    print(img.shape)  # (784,)
    img = img.reshape(28, 28)  # 形状を元の画像サイズに変形
    print(img.shape)  # (28, 28)

    img_show(img)

class NeuralnetMnist:
    """
    MNISTのニューラルネットワーク推論処理
    """
    def __init__(self):
        pass
    def get_data(self):
        (_, _), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
        return x_test, t_test


    def init_network(self):
        with open("sample_weight.pkl", 'rb') as f: # 学習済みの重みパラメータを保存するファイル
            network = pickle.load(f)
        # print(network.keys()) # 全パラメータ確認
        return network

    def print_network_shape(self,network):
        """
        各層の形状を出力する
        """
        W1, W2, W3 = network['W1'], network['W2'], network['W3']
        b1, b2, b3 = network['b1'], network['b2'], network['b3']
        print(f"W1: {W1.shape}")
        print(f"b1: {b1.shape}")
        print(f"W2: {W2.shape}")
        print(f"b2: {b2.shape}")
        print(f"W3: {W3.shape}")
        print(f"b3: {b3.shape}")


    def predict(self,network, x):
        W1, W2, W3 = network['W1'], network['W2'], network['W3']
        b1, b2, b3 = network['b1'], network['b2'], network['b3']

        a1 = np.dot(x, W1) + b1
        z1 = active_func.sigmoid_func(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = active_func.sigmoid_func(a2)
        a3 = np.dot(z2, W3) + b3
        y = active_func.sigmoid_func(a3)

        return y
    
    def run(self):
        x, t = self.get_data()
        network = self.init_network()
        # self.print_network_shape(network)
        accuracy_cnt = 0
        for i in range(len(x)):
            y = self.predict(network, x[i])
            p= np.argmax(y) # 最も確率の高い要素のインデックスを取得
            if p == t[i]:
                accuracy_cnt += 1

        print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
    
    def batch_run(self):
        x, t = self.get_data()
        network = self.init_network()

        batch_size = 100 # バッチの数
        accuracy_cnt = 0

        for i in range(0, len(x), batch_size): # 100枚分ずつで学習する
            x_batch = x[i:i+batch_size]
            y_batch = self.predict(network, x_batch)
            p = np.argmax(y_batch, axis=1)
            accuracy_cnt += np.sum(p == t[i:i+batch_size])

        print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

if __name__ == '__main__':
    # run_mnist()
    # NeuralnetMnist().run()
    NeuralnetMnist().batch_run()
    pass