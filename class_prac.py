'''
python class

일반적인 c++ 이나 java에서 사용되는 class의 개념과 동일함.
인스턴스화 및 oop의 개념에 대한 부분을 python에서도 제공하고 있음

또한 global keyword를 통해 전역 변수도 지원해주고 있음.

'''

result = 0

def adder(num):
    global result
    result += num
    return result


print(adder(2))
print(adder(3))



'''
위의 예제에서 다중 adder가 필요한 경우 별도의 이름으로 함수를 여러개 생성하여 사용하여야 한다. 
class를 통한 인스턴스화로 해당 문제를 해결 할 수 있다.
'''

class Calcul:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calcul()
cal2 = Calcul()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(5))
print(cal2.adder(6))


#pass keyword는 real로다 pass다.
class Simple:
    def sum(self,a,b):
        result = a+b
        print("%s + %s = %s 입니다." % (a, b, result))

test = Simple()
test.sum(10,20)

'''
self는 해당 인스턴스 명을 넘겨주게 된다.
해당 인스턴스 명은 class type을 체크하는 역할을 하는듯 하다. 

self라는 변수를 클래스 함수의 첫번째 인수로 받는것은 파이썬만의 특징이라고 한다. (in jump2python)

getter / setter 이용시 self 는 this 키워드랑 비슷하다고 생각된다. 
python 에도 this 키워드가 있는지 확인필요. 

'''

class Pass:
    pass
    #pass는 임시로 코드 작성시 사용하는 키워드


'''

init 함수는 생성자 함수인듯하다. 
self의 사용에 대해서는 익숙해져야 할듯하다. 
this keyword라기 보다는 뭔가 인스턴스의 id값을 위한 처리라고 생각하는것이 편할 

'''

class Service:
    secret ='this is secret'

    def __init__(self, name):
        self.name = name

    def sum(self, a, b ):
        result = a + b
        print("%s님 %s + %s = %s" %(self.name , a , b , result))


wook = Service('욱')
wook.sum(1,1)
