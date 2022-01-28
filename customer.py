"""
C-1. フルネームを取得できる
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
C-2. 年齢という概念の追加
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す
C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す
C-4. 単一の顧客情報をCSV形式で取得できる
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
応用課題
以降は応用課題です
Customerクラスの実装だけではなく、仕様の理解やどういうふうにクラスを利用するかも含めて考えてください
C-5. 3歳以下の入場料金の無料化
3歳以下の入場料金は無料にしてください
C-6. 75歳以上の料金区分の追加
75歳以上の入場料金は500円にしてください
C-7. 単一顧客の情報取得形式の追加その1
単一顧客の情報取得をタブ区切りにも対応させてください
下記は出力の例
Ken Tanaka  15  1000
Tom Ford    57  1500
Ieyasu Tokugawa	73  1200
C-8. 単一顧客の情報取得形式の追加その2
単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください
下記は出力の例
Ken Tanaka|15|1000
Tom Ford|57|1500
Ieyasu Tokugawa|73|1200
"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return (f"{self.first_name} {self.family_name}")

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif 3 < self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        return (f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}")

    def tab(self):
        return (f"{self.first_name} {self.family_name}\t{self.age}\t{self.entry_fee()}")

    def pipe(self):
        return (f"{self.first_name} {self.family_name}|{self.age}|{self.entry_fee()}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
jun = Customer(first_name="Jun", family_name="Onuma", age=3)
kin = Customer(first_name="Kin", family_name="Gin", age=100)

# 以下、動作確認

# C-1
print(ken.full_name())  # "Ken Tanaka" という値を返す
print(tom.full_name())  # "Tom Ford" という値を返す

# C-2
print(ken.age)
print(tom.age)
print(ieyasu.age)

# C-3
print(f"子供料金は（20歳未満）:{ken.entry_fee()}円")
print(f"おとな料金（20歳以上65歳未満）：{tom.entry_fee()}円")
print(f"シニア料金（65歳以上）：{ieyasu.entry_fee()}円")

# C-4
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())

# C-5
print(jun.entry_fee())

# C-6
print(kin.entry_fee())

# C-7
print(ken.tab())
print(tom.tab())
print(ieyasu.tab())

# C-8
print(ken.pipe())
print(tom.pipe())
print(ieyasu.pipe())
