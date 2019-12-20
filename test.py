print('hello world')
print('나의 이름은 {}입니다'.format('한사람'))
print("test 'String'")

#python 표준 입력 함수 - print()
'''
python3 와 python2 버전의 차이 존재. 
python 기본기능에 대한 학습 진행 
-> tensorflow or 파이토치 or keras 비교분석 후 학습 진행하기 .


python은 인터프리터 언어이다. 
'''
print('하나 둘 셋', end= "->")
print('endtest ,, default 줄바꿈 문자를 교환하는 파라미터 "end" ')



#python2 에서 %를 이용한 변수표현을 하였으나 3버전부터 .format을 많이 쓴다고 한다. 
print('%s씨는 상위 %d%%안에 있는 사람입니다.'%('한사람',10))
print('test {0} , test 2 {1}'.format('test1','test2'))
print('나의 이름은 "{0}"입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('한사람',33,'남성'))
print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7))
print('-' * 40)


#문자열 앞에 0채우기 zfill
print('12'.zfill(4))



'''
길이와 정렬
{:길이} : 출력할 데이터의 길이를 지정합니다. 문자열(왼쪽 정렬), 숫자(오른쪽 정렬)
{:<길이} : 왼쪽 정렬
{:>길이} : 오른쪽 정렬
{:^길이} : 가운데 정렬
'''
print('Python is [{:15}]'.format('good'))




