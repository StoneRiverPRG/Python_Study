# break
# continue

# まずはbreakの使い方
i = 0
while True:
    # 無限ループ
    print(i, end=" ")
    if i == 5:
        print("i==5なのでwhileループをbreakします")
        break
        # breakがあると無限ループから抜ける
    i += 1
print("whileループ終了しました")

# 0 1 2 3 4 5 i==5なのでwhileループをbreakします
# whileループ終了しました

# continue
for j in range(5):
    print("j = " + str(j), end=", ")
    if j == 2:
        print()
        continue
        # contineuでループ１回飛ばし
    print("j * j = " + str(j * j))
    # continueされたループ（j == 2)ではj*jのprintが実行されない

# j = 0, j * j = 0
# j = 1, j * j = 1
# j = 2,
# j = 3, j * j = 9
# j = 4, j * j = 16

# 2重ループでのbreak
for x in range(5):
    # x ループ
    for y in range(5):
        # y ループ
        print("x, y : " + str(x) + ", " + str(y))
        break
        # yループはbreakによりprint関数は最初の１回しか実行されない(y==0だけ)
        # 当然xループはbreakされない。あくまでそのループだけ

# x, y : 0, 0
# x, y : 1, 0
# x, y : 2, 0
# x, y : 3, 0
# x, y : 4, 0

# 2重ループでのcontinue, break
for x in range(5):
    # x ループ
    for y in range(5):
        # y ループ
        if x == 2 or x == 3:
            continue
            # x = 2か,x = 3の時continueの為、
            # 下記プリント関数が実行されない
            # あくまでループ飛ばされるのはyループのみ
        print("x, y : " + str(x) + ", " + str(y))
# x, y : 0, 0
# x, y : 0, 1
# x, y : 0, 2
# x, y : 0, 3
# x, y : 0, 4
# x, y : 1, 0
# x, y : 1, 1
# x, y : 1, 2
# x, y : 1, 3
# x, y : 1, 4
# x, y : 4, 0
# x, y : 4, 1
# x, y : 4, 2
# x, y : 4, 3
# x, y : 4, 4
