"""
ディクショナリー(辞書)
"""
# ディクショナリの新規作成＆初期化
fruits_price = {"バナナ": 100, "りんご": 90, "ぶどう": 500}
# {key: value, key: value, ... }
# 大かっこ？　{ }で囲む
# keyとvalueの集合体

dictionary = {}
# 空のディクショナリはこう作成する

print(fruits_price)
# {'バナナ': 100, 'りんご': 90, 'ぶどう': 500}
# key とvalue の両方が表示される

print(fruits_price["ぶどう"])
# 500
# [key]で指定したvalueを取り出せる

# print(fruits_price["もも"])
# ディクショナリにないkeyはエラーになる
# KeyError: 'もも'

fruits_price["いちご"] = 200
fruits_price["オレンジ"] = 150
# 新しい要素を追加できる

print(fruits_price)
# {'バナナ': 100, 'りんご': 90, 'ぶどう': 500, 'いちご': 200, 'オレンジ': 150}

del fruits_price["りんご"]
# del でkeyの削除
fruits_price.pop("いちご")
# pop関数でも削除できる

print(fruits_price.keys())
# dict_keys(['バナナ', 'ぶどう', 'オレンジ'])
# keyだけが表示される
# りんごといちごが削除された

print(fruits_price.values())
# dict_values([100, 500, 150])
# valueだけが表示される

print(fruits_price.items())
# dict_items([('バナナ', 100), ('ぶどう', 500), ('オレンジ', 150)])
# key とvalue の両方が表示される
# print(fruits_price) とは表記が異なる
print(fruits_price)
# {'バナナ': 100, 'ぶどう': 500, 'オレンジ': 150}

print("バナナは" + str(fruits_price["バナナ"]) + "円です")
# バナナは100円です

fruits_copy = fruits_price
# NG
# 値コピーと思いきやリンクしているので両方変わっちゃう
fruits_copy["バナナ"] = 210

print(fruits_price)
# {'バナナ': 210, 'ぶどう': 500, 'オレンジ': 150}
# オリジナルも210に変わっちゃってる

fruits_copy2 = fruits_price.copy()
# ディクショナリーのコピー
# 値コピーになるのでオリジナルとリンクしない

