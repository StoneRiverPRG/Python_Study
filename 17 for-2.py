"""
for loop -2
"""
# list や辞書のループ処理

strings = "I am a Python programmer."

# リスト
colors = ["red", "blue", "yellow", "black"]

# 辞書
fruits_price = {"バナナ": 100, "りんご": 90, "ぶどう": 500}

# 通常のループ
for i in range(0, 6):
    print(i)
# 0, 1, 2, 3, 4, 5

# 文字列のループ
for s in strings:
    print(s)
# 一文字ずつ取り出される
# I
#  
# a
# m
#  
# a
# ...

# リストのループ
for color in colors:
    print(color)
# リスト１つずつ取り出される
# red
# blue
# yellow
# black

# reversed()関数で逆順にもループできる
for color in reversed(colors):
    print(color)
# black
# yellow
# blue
# red

# enumerate()で要素番号も簡単に取得できる
for i, color in enumerate(colors):
    print(str(i) + "-" + color)
# 0-red
# 1-blue
# 2-yellow
# 3-black

# 辞書のループ
# keyがループされる
for fruit in fruits_price:
    print(fruit)
# バナナ
# りんご
# ぶどう

# values()を使えばvalue だけでのループも出来る
for price in fruits_price.values():
    print(price)
# 100
# 90
# 500

for key, value in fruits_price.items():
    print(key + "-" + str(value))
# バナナ-100
# りんご-90
# ぶどう-500
