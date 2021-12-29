# クラスの最も基本的な使い方

# 定義
class SampleClass:
    pass
	# 何もしないクラスの作成


# クラスを使用する
# インスタンスの生成（この場合test変数がインスタンス）
test = SampleClass()

# メソッドの宣言
# メソッド：クラス内関数のこと


class Sample2:
    msg = "Hello class!"

    # 第一引数にselfをとる
    # 慣例で[self]とする。仮引数とかインスタンス自身とか。
    def test_method1(self):
        print(self.msg)
        # selfを使ってクラス内変数を使える

    def test_method2(self, string):
        print(string)


test2 = Sample2()
test2.test_method1()
# Hello class!

test2.test_method2("dadada")
# dadada

# オーバーロード（同じメソッド名で引数の数が異なる）は出来ない。

# コンストラクタ（インスタンス生成時に呼び出される）
# initメソッドを定義しておく。
# アンダースコア(_)を前後に2つずつ付けるのは
# マジックメソッドというらしい。おまじない。


class Sample3:
    # メンバ変数(クラス変数）：空のリストを生成
	temp = []
	# コンストラクタ__init__(self)を生成。
	# 引数を追加しても良い。

	def __init__(self, number):
		# メンバ変数は「self.」を忘れない
		print("init前tempリスト：" + str(self.temp))
		self.temp.append(1)
		self.temp.append(number)
		# numberはメンバ変数ではないのでself.いらない
	def PrintTemp(self):
		print("temp list:" + str(self.temp))

testclass3 = Sample3(123)
testclass3.PrintTemp()
# init前tempリスト：[]
# temp list:[1, 123]

# クラス変数とインスタンス変数
# クラス変数：クラス依存変数。インスタンスからも呼べる
# インスタンス変数：インスタンスが複数あればそれぞれ異なる値

class testvariavle:
    my_id = 1
    def __init__(self):
        pass

    def printID(self):
        print(self.my_id)

testvar = testvariavle()
testvar.printID()