# 標準入力の取り扱い、sysライブラリ
# readline(), readlines(), read()

import sys
# sysをインポートすることで入力関数群を使用できる　

#####################
# readline()
print("readline()読み込み用に1行入力>>")
line = sys.stdin.readline()
# 標準入力から1行のみ取得。
# 文字列で返す。改行文字込み。
# input()は１行。改行文字削除済み
print("readline()結果：" + line)

#####################
# readlines()
print("readlines()読み込み用に数字を複数行入力>>")
lines = sys.stdin.readlines()
# 標準入力から複数行まとめて取得。
# 行単位でリスト形式。改行文字込み。
print(lines)
# 未処理なので改行文字含まれてる

numbers_list = []
for line in lines:
    number = int(line.rstrip())
    # rstrip()で行末改行削除し、int型へ
    numbers_list.append(number)
print(numbers_list)

#####################
# read()
lines2 = sys.stdin.read()
# 標準入力から複数行取得
# 複数行を１つの文字列としてまとめて取得
print(lines2)

# 指定した回数だけ入力を受け付けたい時
N = 3
# strings = [input("3行入力してください>>").rstrip() for dummy in range(N)]
strings = [sys.stdin.readline().rstrip() for dummy in range(N)]
print("reaadline()結果：" + str(strings))

# import sys
# input_lines = sys.stdin.readlines()
# # print(input_lines)
# nums = []
# n = int(input_lines[0].rstrip())
# for i, line in enumerate(input_lines):
#     if i == 0:
#         continue
#     num = int(line.rstrip())
#     # print(num)
#     nums.append(num)

# # print(nums)
# nums.sort()
# # print(nums)

# for num in nums:
#     print(num)
