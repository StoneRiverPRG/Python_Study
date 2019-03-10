# 複数の条件式

# and
time = 16

if time > 9 and time < 18:
    print("就業時間中だよ")
    # 条件式がどちらもTrueの場合に実行される

# or
time = 15

if time == 10 or time == 15:
    print("おやつの時間だよ！")
    # どちらかが成立すればTrueとなり実行される

# not
time = 9

if not time == 18:
    print("退社時刻ではないよ")
