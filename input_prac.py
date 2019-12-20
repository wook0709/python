"""
help(input)

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

"""

'''
# 표준 입력
print('이름을 입력하세요', end="")
name = input();
print("이름 : {0}, type : {1}".format(name,type(name)))
name = input('이름을 입력하세요 ');
print("이름 : {0}, type : {1}".format(name,type(name)))
name = input('아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요');
'''

# 표준 입력
data = input("정수를 입력하시오 : ")
print(data, type(data))
# print(data, type(data), data + 1) 에러 문자열과 정수를 +(더하기)할 수 없습니다.

#실행할 때 차례대로 1, 2, 3, 1010, 10, 10, 1a를 입력해보세요

#eval() 함수 : 인수를 유효한 파이썬 표현식으로 리턴 합니다.
'''
input을 받을때는 eval로 감싸 받는것이 type 체크를 위해서도 좋을 듯하다. ?

하지만, input()을통 한 입력값 받는것은 연습 외에는 사용하지 않을 듯하다.
'''

data = eval(input('정수를 입력하세요~~ : '))
print(data, type(data))

data = int(input("정수를 입력하시오 : "))
print(data, type(data), data + 1)

data = int(input("2진수를 입력하시오 : "), 2)
print(data, type(data), data + 1)

data = int(input("8진수를 입력하시오 : "), 8)
print(data, type(data), data + 1)

data = int(input("10진수를 입력하시오 : "), 10)
print(data, type(data), data + 1)

data = int(input("16진수를 입력하시오 : "), 16)
print(data, type(data), data + 1)





