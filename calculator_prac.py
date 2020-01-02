class Cal_4:
    def setdata(self, a, b):
        self.first = a
        self.second = b

    def sum(self):
        return self.first+self.second
    def mul(self):
        return  self.first*self.second

Calculator = Cal_4()

print(type(Calculator))
Calculator.setdata(5,10)
print(Calculator.sum())
print(Calculator.mul())


class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s여행을가다" %(self.fullname , where))

wook = HousePark("태욱")
wook.travel("분당")

'''
python도 class를 가지고 OOP를 하는 언어이므로, 
기본적으로 상속의 개념도 가지고 있음.
'''
class HouseNam(HousePark):
    lastname = "남"

nam = HouseNam("태욱")
nam.travel("미금")



'''
상속이 있으므로, overwrite 및 overloading의 개념도 다 가지고 있다11
'''

