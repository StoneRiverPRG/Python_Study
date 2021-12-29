# 関数の基本

"""
関数の基本
"""
print("関数！")


# E302 expected 2 blank lines
# "これは関数と関数の間や、クラスとクラスの間が2行あいてない

# 関数の定義
def microwave():
    print("時間を指定する処理")
    print("温める処理")
    print("温めるのをやめる処理")

microwave()

# TODO: some Todo comment here
# BUG bug comment
# FIXME:fix comment
# HACK: hack
# XXX :xxx commnent
# FIX


def microwave2(mode):
    if(mode == "解凍"):
        print("解凍モードで温める処理")
    elif(mode == "700W"):
        print("700Wで温める処理")
    else:
        print("500Wで温める処理")

microwave2("解凍")
microwave2("700W")
microwave2("aaa")


# 戻り値
def circlearea(radius):
    result = radius * radius * 3.14
    return result


print(circlearea(2))

R1 = circlearea(1.1)
print("半径は%f" % (R1))
