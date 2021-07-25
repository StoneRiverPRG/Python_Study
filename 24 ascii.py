# Ascii　文字の扱い
# ord(), chr()

s = 'A'

ord_s = ord(s)
print(ord_s)  # 65

chr_s = chr(ord_s)
print(chr_s)  # A

print(s, ord_s, bin(ord_s))
# TIPS 0b無しで表示
print(bin(ord_s)[2:])

lower_s = s.lower() # a
print(ord(lower_s)) # 97

# asciiコード + 32 で小文字へ変換
# A → a
print(chr(ord_s + 32)) # a

string = "Hello!"
for ch in string:
    print(ch + " = " + str(ord(ch)) + ", bin = " + str(bin(ord(ch))))