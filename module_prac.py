#help("modules")
'''

import를 통해서 modules들을 사용할 수 있다.
as 를 통해 모듈명 변경이 가능함.
'''

import datetime
import math
import math as m
from math import *

# import datetime
now = datetime.datetime.now()
print(now)

# import math
print("The value of pi is", math.pi)

# import math as m
print("The value of pi is", m.pi)

# from math import pi
print("The value of pi is", pi)

# from math import *
print("The value of e is", e)

from Module.mod1 import sum
#from Module import mod1
print(sum(1, 3))

'''개인이 만든 module도 경로만 잘 맞추어서 사용하면 ok!
 -> 폴더를 만들면 from 폴더명 import 모듈명으로 사용하면 된다. 
 -> 위의 예시처럼 . 으로 모듈명을 선언하고 특정모듈함수를 import 해서 사용가능하다. 
 -> 또는 from mod1 import * 로 모두 import가 가능하다. 
'''


"""
KEYWORD는 다른 언어와 마찬가지로 예약어 이다. 

1. TRUE / FALSE 
2. None - 값이 없음을 표현하는 방식이다 . 0 or False 와는 다른 값이다.  

   ** ※ 3항 연산자 : 연산 대상이 3개인 연산자 -> 참일때 값 if 조건 else 거짓일때값 
   print("값이없음" if result==None else result) - in python
   

3. assert : debug용으로 사용되는 키워드 
   사용형식 : assert condition, message
   
   
   
"""


