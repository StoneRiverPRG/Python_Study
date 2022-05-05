import heapq
# ファイル名をheapq.pyとするとはまるので注意
# （ライブラリ名と同じファイル名にはしない！）
#  partially initialized module 'heapq' has no attribute 'heappush' (most likely due to a circular import)

# ヒープキューの使い方と2次元リストへの応用法

# ヒープとは

# キューとは

# ヒープ＋キュー = heapqライブラリとは

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
# なぜ高速か

# 実用例

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
print(heapq.heappop(heap_list_in_list))
print(heapq.heappop(heap_list_in_list))
print(heapq.heappop(heap_list_in_list))
# print(heapq.heappop(heap_list_in_list))
# IndexError: index out of range
# heapのリストが空の場合取り出せない(pop)のでエラー

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

print(min_value)
# [[4, 'apple', 1]]
# 要素3番目x[2]が比較されて最小値1の要素が表示された
# nsmallestがn個の
print(heap_list_in_list)
# [[-1, 'zzzz', 999], [4, 'apple', 1], [30, 'banana', 100]]
# popではないので要素数は減っていない

max_value = heapq.nlargest(1, heap_list_in_list, key=lambda x:x[2])
print(max_value)

# 例題
import random
import pprint
# 2次元リストprint整形用

monster = []
for i in range(10):
    x = random.randint(0, 400)
    y = random.randint(0, 300)
    level = random.randint(1, 99)
    entity = (x, y, level)
    monster.append(entity)

print("monsterリストの表示")
pprint.pprint(monster)

print("")

monster_for_heap = [(value[2], value) for value in monster]
print("monster_for_heap : heapq用にkeyを設定したリスト（heapify前）")
pprint.pprint(monster_for_heap)

print("")

# 最大5個分
big5 = heapq.nlargest(5, monster, key= lambda x:x[2])
print("monster : level big 5")
pprint.pprint(big5, width=20)
#[(293, 184, 97),
# (351, 195, 97),
# (101, 276, 96),
# (150, 197, 93),
# (346, 184, 92)]

print("")

# 最小5個分
min5 = heapq.nsmallest(5, monster, key= lambda x:x[2])
print("monster : level small 5")
pprint.pprint(min5, width=20)
#[(293, 184, 97),
# (351, 195, 97),
# (101, 276, 96),
# (150, 197, 93),
# (346, 184, 92)]

print("")


heapq.heapify(monster_for_heap)
print("monster_for_heap =")
pprint.pprint(monster_for_heap)

print("")

print("heappopで5回データ取り出し")
for i in range(5):
    _, monster2 = heapq.heappop(monster_for_heap)
    print(monster2)
