"""
複数行コメントアウト
コメントアウト
セミコロンはいらない
Python3では# coding: utf-8いらなくなった
"""

# 一行コメントアウト

# printf
print("Hello World!")
# \n 改行, \t タブ
print("Hello \tWorld!\n")
Name = "Ishikawa"
Age = 34
Score = 99.4
# %で文字列埋め込み
print("Name:%s, Age = %d, score = %f" % (Name, Age, Score))
print("Name:%10s, Age = %4d, score = %10.3f" % (Name, Age, Score))
# format {}で指定
print("Name:{0}, Age = {1}, score = {2}" .format(Name, Age, Score))
print("Name:{0:10s}, Age = {1:10d}, \
    score = {2:10.4f}" .format(Name, Age, Score))
# >右揃え <左揃え
print("Name:{0:>10s}, Age = {1:<10d}, \
    score = {2:>10.4f}" .format(Name, Age, Score))

# %-10 -で左寄せ
print("Name:%-10s, Age = %-4d, score = %-10.3f" % (Name, Age, Score))

# 変数
str = "Hey!"
print(str)

str = "HeyHeyHey!"
print(str)

i = 10
f = 3.14
# 論理値 大文字で！
b1 = True
b2 = False

x = 20
y = x / 3
print(y)
print(x / 3)
# 切り捨て除算 10 // 3 = 3
print(x // 3)

print(True and False)  # False
print(True or False)  # True
print(False or False)  # False
print(not True)  # False

print("Hello" + "world")
str2 = "Hey"
print(str2 * 5)  # HeyHeyHeyHeyHey
print(str + str2 * 3 + "!")

# 切り捨て除算
# print(x　//　3)
# 定数
ISHIKAWA = "石川"
print(ISHIKAWA)


# if分
test = 80

if test > 80:
    print("Great!")
elif test > 60:  # else if
    print("Nice!")
else:
    print("So So!")

# 条件演算子
print("Great!" if test > 80 else "so so! ..")

# While ループ
print("While ループ")

i = 0
name = "ishikawa"

while i < 10:
    # if i == 5:
        # break
    print("%d:%s" % (i, name))
    i = i + 1
else:
    print("finish!")


# for文
print("for文")
for i in range(0, 10):
    print("i=%d" % (i))
    # if i == 5
    print("HE")

else:
    print("Finish!")

def test():
    print("テスト関数")

# コード中に改行　"\"
cube_directions_a = [ (+1, -1, 0), (+1, 0, -1), (0, +1, -1), (-1, +1, 0), (-1, 0, +1), (0, -1, +1)]
# 長いと見ずらい！ので、\ で改行できる。
cube_directions_b = [ (+1, -1, 0), (+1, 0, -1), \
                    (0, +1, -1), (-1, +1, 0), \
                    (-1, 0, +1), (0, -1, +1)]

