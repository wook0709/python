

#파일쓰기
f = open("/Users/wook/PycharmProjects/python/test.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)

f.close()

"""
외부파일을 읽는 여러가지 방법들 

일반적으로 c 등에서 사용되는 파일 읽기 방법이랑 동일하다. 

1.readline() - 한줄 읽기
   -> while 문을 통해서 파일 전체 읽기도 가능 
   
    f = open("파일경로",'r')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close
    
    -> 더이상 읽을 line이 없는 경우 None을 반환한다.
     
"""

#파일 읽기

f = open("/Users/wook/PycharmProjects/python/test.txt",'r')

'''
#다중 읽기도 가능

lines = f.readlines()
for line in lines:
    print(line)
'''
while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()


#with 를 통한 자동 파일 close기
#with 구문은 python 2.5 부터 지원
with open("/Users/wook/PycharmProjects/python/test.txt",'r') as f:
    lines = f.readlines()
print("with 구문을 통한 파일 읽기")
print(lines)





