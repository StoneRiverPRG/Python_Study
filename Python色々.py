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


# 文字列スライス
maybe = "It's raining, maybe."
# 後ろから8文字削除
must = maybe[:-8] + "!!"
print(must)
# It's raining!!

# 四捨五入
# 組み込み関数round 厳密には四捨五入ではない
pi = 3.14
print(round(pi))
# 3

print(round(pi, 2))
# 3.14


########################
"""
アンダースコアの使い場所
1.Return値を無視する。
2.関数の名付けで使い方を区別する。
3.数字を読みやすくする。
4.インタプリタで最後に表示された値を代表する。

２、関数の名付けで使い方の区別
関数の名付けで使うアンダースコアは、アンダースコアの付ける位置と数で関数の使い方を4種類に区別します。それぞれPEP8のコーディング規約で定義されています。
a、_function(x): #関数前に一つ
def _single_leading_underscore(x):
    return something
# weak "internal use" indicator. E.g. from M import * does not
# import objects whose names start with an underscore
関数前に一つアンダースコアを付ける事により、関数を”内部用”に定義できます。他のプログラミング言語のPrivate属性と似たような物ですが、Pythonには事実上のPrivate属性がありません。PEP8の説明ではweak internal useと説明されていて、from M import * の時、では一つのアンダースコアで始まる関数はインポートされませんが、class内の関数だとclassx._func()で関数を呼ぶ事が出来ます。
b、function_(x): #関数後に一つ
def single_trailing_underscore_:
    return something
# used by convention to avoid conflicts with Python keyword, e.g.
# Tkinter.Toplevel(master, class_='ClassName')
関数後に一つアンダースコアを付けるのはPython内の重要関数と名付けを被らせない為です。例えばclass内でどうしてもlistと言う関数や引数を設定したい時は list_ と名付けてPythonのlistと被ることを避けます。
c、__function(x): #関数前に二つ
def __double_leading_underscore:
    return something
# when naming a class attribute, invokes name mangling
# (inside class FooBar, __boo becomes _FooBar__boo; see below).
class内の関数前に二つアンダースコア付けることで、名前の マングリング機構を呼び出します。ここのマングリングとは、インタプリタやコンパイラーが普通の方法で変数を扱わなくなる事です。例えばclass FooBarの関数__booについて、Foobar.__barでは関数を呼べ出せなく、_Foobar__booという使い方になります。擬似的にPrivate属性を作れます。
d、__function__(x): #関数前後に二つずつ
def __double_leading_and_trailing_underscore__:
    return something
# "magic" objects or attributes that live in user-controlled
# namespaces. E.g. __init__, __import__ or __file__. Never invent
# such names; only use them as documented.
class内の関数の前後に二つずつアンダースコア付けることで、magic methodになります。__init__や__call__、__iter__等既存のmagic methodがあってクラスを華やかに書けますが、普段の開発では自分で新しく定義しないことをお勧めします。
"""


# alphabet = ["A", "B", "C", "D", ...]
# 面倒くさいけど、これなら簡単に
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet)

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
