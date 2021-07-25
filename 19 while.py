"""
while ループ
"""

# while の書式
# while 条件式:
#     繰り返し処理
#     カウンタ変数を更新

i = 1  # カウンタ変数の初期化
while i <= 5:  # 1, 2, 3, 4, 5, 6
    print(i)
    i += 1
    # i = i + 1と同じ
    # i -= 1 もあるよ
"""
1
2
3
4
5
"""

# iが6になったのでwhileループから出た
print("i = " + str(i))
# i = 6


# スライムを攻撃
# ダメージは1から10までランダム
# スライムのHPが0になるまで繰り返す

from Lib import random
hp = 20
while hp > 0:
    hit = random.randint(1, 10)
    print("スライムに" + str(hit) + "のダメージを与えた！", end="")
    hp -= hit
    print("(hp" + str(hp) + ")")
print("スライムを倒した！")

"""
スライムに7のダメージを与えた！(hp13)
スライムに3のダメージを与えた！(hp10)
スライムに1のダメージを与えた！(hp9)
スライムに2のダメージを与えた！(hp7)
スライムに10のダメージを与えた！(hp-3)
スライムを倒した！
"""


for i in range(1, 6):
    print(i)
