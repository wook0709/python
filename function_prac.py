'''
파이썬 함수 구조는

def 함수명(입력인수):
    수행문장1
    return 결과값

'''

def sum(a,b):
    return a+b

out = sum(4,5)
print(out)


'''
#파일 입출력

f = open("파일.txt", 'w')

f.close()

-> filestream을 그냥 open으로 열고, option으로 mode 값을 셋팅한다. 

mode - r / w / a ( read / write / append )
'''