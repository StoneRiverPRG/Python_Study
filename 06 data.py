# データ型

# データ型の違い
# 数値型の計算
print(3 + 7)
# 10

# 文字列型の計算（連結）
print('3' + '7')
# 37

# str型
price = 110
# 文字列型＋数値型＋文字列型
# print("ジュースの価格は" + price + "円です。")
# エラーになってしまう！

# 文字列型＋文字列型＋文字列型
# str()で文字列型に変換する
print("ジュースの価格は" + str(price) + "円です。")
# ジュースの価格は110円です。

# int型
count = '3'
price = 110
# int()で数値型に変換
total_price = price * int(count)
print(total_price)
# 330

# float型
pi = 3.1415
print(pi)
# 3.1415

# 正n角形の内角1つの角度を計算
n = 6
sou_kakudo = 180 * (n -2)
naikaku = sou_kakudo / n
print("内角の合計は" + str(sou_kakudo) + "°")
print("正n角形の1つの内角は" + str(naikaku) + "°")
# 内角の合計は720°
# 正n角形の1つの内角は120.0°
