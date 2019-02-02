# 配列 list の基礎
print("配列！")

# 配列の宣言(空の配列、宣言と同時に初期化)
list = []
list2 = [1, 1, 2, 3, 5]

# 要素の追加
print(list2)
list2 = list2 + [8, 13, 21]
print("要素追加後")
print(list2)

# 要素の追加（別の方法）
list2 = [10, 20, 30]
list2.append(40)
print(list2)

list2.insert(2, 21)
print(list2)
list2.insert(0, 0)
print(list2)

# 要素数の取得( len()関数)
print(len(list2))

# 要素の削除(del文, popメソッド)
list = [1, 2, 3, 4, 5]
print(list)
del list[3]
print(list)

list = [1, 2, 3, 4, 5]
print(list)
list.pop(3)
print(list)
