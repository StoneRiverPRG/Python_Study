# elif
# 複数の条件式

score = 70
if score == 100:
    print("満点です！")

elif score >= 60:
    # elif (else ifの意味)
    print("まずまずの点数")

else:
    print("赤点だよ！")

# まずまずの点数

# elifは何回も書ける
score = 70
if score == 100:
    print("満点です！")
elif score >= 70:
    print("おしい！")
elif score >= 60:
    print("まずまずの点数")
else:
    print("赤点だよ！")

# おしい！
