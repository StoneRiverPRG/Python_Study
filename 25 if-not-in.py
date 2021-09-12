# if の便利な使い方

# if A in B
fruits = ["ぶどう", "いちご", "桃", "バナナ"]

# "みかん" は リスト fruitsにあるかどうか

if "みかん" in fruits:
    # fruits にみかんがあるとき
    result = True
else:
    result = False
print(result)
# False

# これだけで表現できます
# もしif A in B を知らないと。。。

for f in fruits:
    if f == "みかん":
        result = True
    else:
        result = False
print(result)
# False

# for in ループをする必要があります。

# ＡがＢにないときの構文
if "メロン" not in fruits:
    # fruits にメロンがないとき
    print(True)
# True

# if A not in B 構文が使えます。
# リストとの相性が良いです。

# if A (not) in Bの使用例
name = "StoneRiver"
nickname = ""
# 子音リスト（大文字、小文字）
voiceless = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]

for s in name:
    if s not in voiceless:
        # s が子音じゃないとき
        nickname += s
    else:
        print(str(s) + "は子音なので除去します")

print(nickname)
# oは子音なので除去します
# eは子音なので除去します
# iは子音なので除去します
# eは子音なので除去します
# StnRvr

# o, e, i, e が除去された