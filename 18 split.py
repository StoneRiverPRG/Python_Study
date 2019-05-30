# str.split()
# 文字列の分割 - 標準ライブラリ

string = "I am a Python3 programmer."

print(string.split())
# ['I', 'am', 'a', 'Python3', 'programmer.']
# 空白で文字列を分割しリスト型で返す

string = "勇者,戦士,魔法使い,盗賊"
team = string.split(",")
# str.split(sep) sepには任意の文字列を指定できる
# 例) str.split(",")
# , で分割して、リストに代入
print(team)
# ['勇者', '戦士', '魔法使い', '盗賊']

print("teamの要素数は" + str(len(team)))
# 4
# teamの要素数

numbers = "3,5,10"
a, b, c = numbers.split(",")
# splitで分けていっぺんに変数a,b,cに代入
sums = int(a) + int(b) + int(c)
# int型の数値にして合計を計算
print(sums)
# 18

# 空白で分けられた数字の合計を計算
numbers = "1 2 3 4 5 6 7 8 9 10"
numberslist = numbers.split()
print(numberslist)

sums = 0
# リストなのでfor in:でループして合計を計算
for number in numberslist:
    sums = sums + int(number)

print(sums)
# 55
