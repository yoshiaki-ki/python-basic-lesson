"""
    Class 2
"""
"""
   多重継承
"""
class Person:
    def talk(self):
        print('talk')

class Car:
    def run(self):
        print('car run')

class PersonCarRobot(Person,Car):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

"""
    クラス変数
"""

class Human:
    kind = 'human'  # クラス内で共通して使われる変数。リストなどをここで指定すると、全てのオブジェクトで共有されるリストとなるため注意

    def __init__(self,name):
        self.name = name # 初期化するため、この変数は各オブジェクトで別物となる

    def who_are_you(self):
        print(self.name, self.kind)

a = Human('Mike')
a.who_are_you()
b = Human('Taro')
b.who_are_you()