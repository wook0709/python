'''
파이썬의 변수는 변수선언, 초기화를 할 필요가 없다.
(인터프리터라서 그런가.. ?)

변수에 값을 할당 할때, 메모리 공간을 예약한다. ( stack ? heap ? )

변수의 다중할당도 가능 ex) a=b=c="같은값" // d,e,f = "값" , 23, 123.23
'''


'''
if 처리 

python에서 if를 사용할 때는, 들여쓰기를 잘 사용해야한다. 

    ex) 
    if 조건문:
        수행 A
        수행 B
        수행 C
    else:
        수행 D
        수행 E
'''

count = 1

if count:
    print('출력')
    print('출력2')
#        print('error')
else:
    print('else')




'''
들여쓰기의 경우는 Tap 이냐 공백이냐 ?
    -> 한가지로만 사용하자 !! , 섞어서 쓰지는 말자 !! 
    -> 공백 4개를 추천한다고 한다. 개취 
    
    대괄호를 안쓰는데서 오는 혼란은 조금 감안해야 할듯 하다. 
'''

#and , or , not 연산자
'''
x or y : x 나 y 중 하나라도 참 
x and y : x, y 모두 참
not x : x가 거짓이면 참
'''

# x in s , x not in s
'''
x in list/튜플/문자열 
x not in list/튜플/문자열
'''
money = 1
if money in [1,2,3]:
    print('in')


pocket = ['money', 'cellphone', 'paper']

if 'money' in pocket: print('get in the TAXI')
else: print('walk')


'''
elif :  파이썬의 else if 문장
        elif 이전 조건문이 거짓일때 수행 된다. 
        
    if 조건:
        수행1
    elif 조건:
        수행2
    elif 조건:
        수행3
    else:
        수행A
        
    -> 위와 같은 조건식으로 작성된다. 
    -> elif는 개수에 제한없이 사용할 수 있다.     
'''


#while문
'''
    while 조건문:
        문장1
        문장2
        문장3
        
    => 조건/반복문의 구성은 동일하다.
    
'''
hit = 0
while hit < 10:
    hit = hit + 1
    print('나무를 %d번 찍었습니다.' % hit)
    if hit == 10:
        print('나무를 쓰러뜨렸습니다.')


prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    
    Enter number :
"""
'''
number = 0
while number != 4:
    print(prompt)
    number = int(input())
'''

#break 도 존재한다

coffee = 10
money = 300

while money :
    print('커피 내립니다.')
    coffee = coffee - 1
    print('남은 커피의 양은 %d' % coffee)

    if not coffee:
        break




""" for 문장 

for 변수 in 리스트 (또는 튜플 , 문자열 ):
    수행할문장 1
    수행할문장 2
    ...
"""

for i in ['one' , 'two' , 'three']:
    print(i)



#튜플형태를 대입하여 출력도 가능하다.

a = [(1,2),(3,4),(5,6)]
for (first, last) in a: #in ([1, 2], [3, 4], [5, 6]):
    print(first+last)
