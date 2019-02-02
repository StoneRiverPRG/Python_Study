# For ループの基礎文法

print("Forループの文法")

words = ['Japanese', 'English', 'French', 'Chinese']

for w in words:
    print(w)

for num in range(5):
    print(num)

for num in range(5, 10):
    print(num)

for num in range(0, 10, 3):
    print(num)

for num in range(20):
    print(num)
    if num == 10:
        print("%dだよ\n" % (num))
        # break
