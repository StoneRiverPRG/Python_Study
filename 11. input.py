# input

input_count = input("購入するみかんの個数を入力して下さい：")
# コンソールから自由に入力を受け取り、変数countに代入される

print("購入するみかんの個数は" + input_count + "個です")
# input("")で代入した値countは文字列型(str)

mikan_price = 120

count = int(input_count)
# 入力した値を数値型に変換して代入

total_price = mikan_price * count
# total_price = mikan_price * input_count
# これだとおかしくなるぞ！

print("お支払い金額は" + str(total_price) + "円です。")
