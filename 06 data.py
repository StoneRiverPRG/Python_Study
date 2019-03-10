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
print("ジュースの価格は" + str(price) + "円です。")
# ジュースの価格は110円です。

# int型
count = '3'
price = 110
# int()で数値型に変換
total_price = price * int(count)
print(total_price)
# 330
