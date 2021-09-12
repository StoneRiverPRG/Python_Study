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
