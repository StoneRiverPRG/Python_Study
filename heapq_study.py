import heapq
# ファイル名をheapq.pyとするとはまるので注意
# （ライブラリ名と同じファイル名にはしない！）
#  partially initialized module 'heapq' has no attribute 'heappush' (most likely due to a circular import)

# ヒープキューの使い方と2次元リストへの応用法(keyの指定）

# ヒープとは
# heap : 積み重ねたもの

# キューとは
# キュー（先入れ先出し）、スタック（後入れ先出し）

# ヒープ＋キュー = heapqライブラリとは
# 優先度付きキュー

# heapqライブラリのオーソドックスな使い方
# 最小値を取り出したいリストを準備
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

# リストをヒープキュー化 （test_list[0]を最小値に）
heapq.heapify(test_list)
print(test_list)
# [1, 1, 2, 3, 3, 8, 4, 6, 5, 5, 5, 9, 9, 7, 9]
# ※ソートではないので小さい順に並ぶ訳ではない！

# 最小値の取り出し（test_list[0]の取り出し）(削除)
# 先に必ずheapifyしておかないと最小値出てこない.
# データ要素の削除を行いたくないときは要素0を表示する
print(test_list[0])
# 1
min_value = heapq.heappop(test_list)
print(f"min_value = {min_value}")
# min_value = 1

print(test_list)
# [1, 3, 2, 3, 5, 8, 4, 6, 5, 5, 9, 9, 9, 7]
# 1つ取り出したことでまた並び順が変わった.
# 取り出しと同時に削除も行っているので, リストの要素数も1個減っている.
# ※くどいですがtest_list[0]が最小値になってる.

# もう一回取り出し確認
min_value = heapq.heappop(test_list)
print(f"min_value = {min_value}")
# min_value = 1

print(test_list)
# [2, 3, 4, 3, 5, 8, 7, 6, 5, 5, 9, 9, 9]
# 1つ取り出したことでまたまた並び順が変わった.
# リストの要素数も1個減っている.
# ※くどいですがtest_list[0]が最小値になってる.

# heapq.heappush
# 値のpush. test_listへデータ入力と同時にリスト先頭値が最小に.
heapq.heappush(test_list, 0)
print(test_list)
# [0, 3, 2, 3, 5, 8, 4, 6, 5, 5, 9, 9, 9, 7]
# 1個増えた. 先頭が今入れた0（最小値）になった.

heapq.heappush(test_list, 7)
print(test_list)
# [0, 3, 2, 3, 5, 8, 4, 6, 5, 5, 9, 9, 9, 7, 7]
# 1個増えた.

# heapq.heappushpop
# pushしてからpopする関数
min_value = heapq.heappushpop(test_list, 10)
print(f"min_value = {min_value}")
print(test_list)
# min_value = 0
# [2, 3, 4, 3, 5, 8, 7, 6, 5, 5, 9, 9, 9, 7, 10]
# プッシュ（入れて）してからポップ（出して）なので要素数変わらず.

# heapq.nsmallest
# 最小値順にn個の値を"リスト"で返す関数
# ちなみにkey指定も出来る.
# popじゃないのでデータは削除されない
small_list = heapq.nsmallest(3, test_list)
print(small_list)
# [2, 3, 3]
print(test_list)
# [2, 3, 4, 3, 5, 8, 7, 6, 5, 5, 9, 9, 9, 7, 10]

print("")

# heapq.nlargest
# 今度はn個の大きい値を"リスト"で返す関数
# こちらもkey指定出来る.
# popじゃないのでデータ削除されないのもnsmallestと同じ
big_list = heapq.nlargest(3, test_list)
print(big_list)
# [10, 9, 9]
print(test_list)
# [2, 3, 4, 3, 5, 8, 7, 6, 5, 5, 9, 9, 9, 7, 10]
print(heapq.nlargest(3, [0, 4, 2, -1, 8, 1]))
# [8, 4, 2]
# heap化されていなくても使える
print("")

# リストインリスト（2次元リスト）での例

# テスト1
heap_list_in_list = []
# 空のリストに最初からheappushするならheapifyは不要
heapq.heappush(heap_list_in_list, [4, "apple", 1])
heapq.heappush(heap_list_in_list, [-1, "zzzz", 999])
heapq.heappush(heap_list_in_list, [30, "banana", 100])
# heapリストの中の各要素は数字でもリスト（2次元リスト）でも良い
# 2次元リストの場合各リストの先頭で要素大小が比較される.
# key = lambda x:x[2] 等で比較要素は指定できない模様

print(heap_list_in_list)
# [[-1, 'zzzz', 999], [4, 'apple', 1], [30, 'banana', 100]]
print(heapq.heappop(heap_list_in_list))
# [-1, 'zzzz', 999]
print(heapq.heappop(heap_list_in_list))
# [4, 'apple', 1]
print(heapq.heappop(heap_list_in_list))
# [30, 'banana', 100]
# ※ 先頭要素の -1 -> 4 -> 30の順になった。
# print(heapq.heappop(heap_list_in_list))
# IndexError: index out of range
# 要素3つしかないので4回目のpopでは
# heapのリストが空で取り出せない(pop)のでエラー

# テスト2
heap_list_in_list = []
# 空のリストに最初からheappushするならheapifyは不要
heapq.heappush(heap_list_in_list, [4, "apple", 1])
heapq.heappush(heap_list_in_list, [-1, "zzzz", 999])
heapq.heappush(heap_list_in_list, [30, "banana", 100])


min_value = heapq.nsmallest(1, heap_list_in_list, key= lambda x:x[2])
# ラムダ関数で各要素の3番目 x[2] で比較するようkey指定
# min_value = heapq.nsmallest(1, heap_list_in_list)
# key不要（リストの先頭で比較）の場合は引数なしでOK
# ちなみにn = 1を指定した場合はmin()の方が早いらしい

print(min_value)
# [[4, 'apple', 1]]
# 要素3番目x[2]が比較されて最小値1の要素が表示された

print(heap_list_in_list)
# [[-1, 'zzzz', 999], [4, 'apple', 1], [30, 'banana', 100]]
# popではないので要素数は減っていない

max_value = heapq.nlargest(1, heap_list_in_list, key=lambda x:x[2])
print(max_value)

# 使用例
import random
import pprint
# 2次元リストprint整形用

# (x, y)座標に出現したモンスターのレベル(Lv)
# (x, y, Lv)のタプルを管理するリストを想定
# 低いレベルのモンスターを3匹ターゲットに選びたい
# モンスターリスト
monsters = []
for i in range(10):
    x = random.randint(0, 200)
    y = random.randint(0, 100)
    level = random.randint(1, 99)
    entity = (x, y, level)
    monsters.append(entity)

print("monstersリストの表示")
pprint.pprint(monsters)
# [(55, 40, 86),
#  (164, 29, 63),
#  (196, 100, 77),
#  (31, 82, 61),
#  (121, 32, 54),
#  (91, 48, 4),
#  (36, 36, 96),
#  (126, 29, 91),
#  (26, 92, 20),
#  (93, 71, 89)]

print("")

# heapifyにkey指定が出来ないのでkey（レベル）を先頭に持ってきた専用リストを作成
# (key, (x, y, Lv))
# 例：元データ (139, 17, 42) → heap用 (42, (139, 17, 42))
monsters_for_heap = [(value[2], value) for value in monsters]
print("monsters_for_heap : heapq用にkeyを設定したリスト（heapify前）")
pprint.pprint(monsters_for_heap)
# [(86, (55, 40, 86)),
#  (63, (164, 29, 63)),
#  (77, (196, 100, 77)),
#  (61, (31, 82, 61)),
#  (54, (121, 32, 54)),
#  (4, (91, 48, 4)),
#  (96, (36, 36, 96)),
#  (91, (126, 29, 91)),
#  (20, (26, 92, 20)),
#  (89, (93, 71, 89))]
print("")

# 最大3個分
# heapq.nlagestは元々key指定できる.
big3 = heapq.nlargest(3, monsters, key= lambda x:x[2])
print("monster : level big 3")
pprint.pprint(big3, width=20)
# [(36, 36, 96),
#  (126, 29, 91),
#  (93, 71, 89)]
print("")

# 最小3個分
# heapq.nsmallestは元々key指定できる.
min3 = heapq.nsmallest(3, monsters, key= lambda x:x[2])
print("monster : level small 3")
pprint.pprint(min3, width=20)
# [(91, 48, 4),
#  (26, 92, 20),
#  (121, 32, 54)]

print("")

# heap化
heapq.heapify(monsters_for_heap)
print("monsters_for_heap =")
pprint.pprint(monsters_for_heap)
# [(4, (91, 48, 4)),
#  (20, (26, 92, 20)),
#  (77, (196, 100, 77)),
#  (61, (31, 82, 61)),
#  (54, (121, 32, 54)),
#  (86, (55, 40, 86)),
#  (96, (36, 36, 96)),
#  (91, (126, 29, 91)),
#  (63, (164, 29, 63)),
#  (89, (93, 71, 89))]
print("")

print("heappopで3回データ取り出し")
for i in range(3):
    _, monster2 = heapq.heappop(monsters_for_heap)
    # heap用に(key, 元list)のタプルを作成したので、
    # key分は捨てる（アンダーバーに代入するが使わない）
    print(monster2)
# (91, 48, 4)
# (26, 92, 20)
# (121, 32, 54)


# ちなみにsortでも出来る
print(sorted(monsters, key = lambda x: x[2]))
# [(91, 48, 4),
#  (26, 92, 20),
#  (121, 32, 54),
#  (31, 82, 61),
#  (164, 29, 63),
#  (196, 100, 77),
#  (55, 40, 86),
#  (93, 71, 89),
#  (126, 29, 91),
#  (36, 36, 96)]