# 文字列
# 文字列の連結

# + で文字列を連結する
print("Hello " + "World!")
# Hello World!

# * で複数回連続表示できる
print("Hello " * 4)
# Hello Hello Hello Hello

name = "Stone"

# 文字列と文字列が入った変数の連結
print("My name is " + name)
# My name is Stone

# 変数に連結した文字列を代入
mynameis = "My name is " + name
print(mynameis)
# My name is Stone

# 長い文字列は"""　トリプルクオートで囲う
longstr = """aaa,
iii,
uuu"""
print(longstr)
#aaa,
#iii,
#uuu

#改行やタブ、スペースもそのまま表示される
longstr = """
    aaa
    bbb
    ccc"""
print(longstr)
#    aaa
#    bbb
#    ccc
