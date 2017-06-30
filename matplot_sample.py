import numpy as np
import matplotlib.pyplot as plt

class Main:

    def showSin(self):
        # データの作成
        x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
        y = np.sin(x)

        # グラフの描画
        plt.plot(x, y)
        plt.show()

    def showCos(self):
        # データの作成
        x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
        y = np.cos(x)

        # グラフの描画
        plt.plot(x, y)
        plt.show()

# Main().showSin()

Main().showCos()
