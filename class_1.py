"""
    Class
"""
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self,age=1):
        self.age = age

    @abc.abstractmethod  # 抽象クラス：継承するクラスで必ず実装が必要となるメソッド
    def drive(self):
        if self.age >= 18:
            print("drive OK")
        else:
            raise Exception("No Drive")

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self): # 継承元のクラスが抽象クラスとなっていて、driveメソッドは実装必須になる
        raise Exception("No Drive")

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self): # 継承元のクラスが抽象クラスとなっていて、driveメソッドは実装必須になる
        print('ok')

baby = Baby()
adult = Adult()
adult.drive()

class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self,person):
        person.drive()

car = Car()
car.ride(adult)

class TeslaCar(Car):
    def __init__(self, model='model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run  # 読み込み専用にする

    # 読み込み専用にする場合の設定
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # プロパティ設定で値を設定できるようにする
    @enable_auto_run.setter
    def enable_auto_run(self,is_enable):
        self._enable_auto_run = is_enable

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar()
print(tesla_car._enable_auto_run)

# __（アンダースコア）が２つの場合、クラス内では参照できる。外で呼び出すことはできない
