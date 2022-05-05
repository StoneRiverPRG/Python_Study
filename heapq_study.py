import heapq

# ヒープキューの使い方と2次元リストへの応用法

# ヒープとは

# キューとは

# ヒープ＋キュー = heapqライブラリとは

# heapqライブラリのオーソドックスな使い方
# test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
# heapq.heapify(test_list)
# print(test_list)
a = []
heapq.heappush(a, 1)
# なぜ高速か