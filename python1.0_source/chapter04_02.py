# Chapter04-2
# 파이썬 반복문
# FOR 실습
'''
# For 흐름제어 실습
 - 반복문 중요성
 - 기본 For 사용
 - For 문 패턴 실습
 - For - Else 구문
'''
# 코딩의 핵심 
# for i in <collection>
#     <loop body>

for v1 in range(10): # range(start, stop, step)
    print("v1 is :", v1)

print()

for v2 in range(1, 11):
    print("v2 is :", v2)

print()

for v3 in range(1, 11, 2):
    print("v3 is :", v3)

print()

for v4 in range(1, 11, 3): # 콜렉션 형태 - 집합의 모음(리스트, 튜플, 딕셔너리 등 여러개의 데이터를 포함할 수 있는 것들)
    print("v4 is :", v4)

print()

# 1 ~ 1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum1)
print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # sum(리스트)
print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))

su=0
a=0
for v in range(1, 1001, 4) :    
    su = su+v
    a += v
    print(v)
    print('1 ~ 1000안에서 4의 배수의 합 :', su, a, sum(range(1, 1001, 4)))


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)


# 예제2_2 로또번호 당첨
import random
print()
print('============================================================')
a = range(1,46)
for i in range(1,7) :
    print('오늘의 로또', i ,'번째 숫자는 : ', random.randrange(1,46))
print('============================================================')

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}
print()
print('----------------------------------------')
# 딕셔너리를 키 : 밸류의 형태로 불러오기 위해서는 dict.keys()와 dict.values()를 알아야 한다.
# 키 값이나 밸류값을 인덱스 번호로 불러오기 위해서는 list로 형 변환을 해준 뒤 인덱스 번호로 불러올 수 있다. 
a=0
for k in my_info:
    print(a+1, k,':', my_info[k])
    a += 1

print()    
print(list(my_info.keys())[0])
print()

a=0
for v in my_info.values():
    print(a+1, list(my_info.keys())[a], ':', v)
    a += 1
print()
print('------------------------------------------')


for key in my_info:
    print(key, ":", my_info[key])

for val in my_info.values():
    print(val)

# 예제5
name = 'FineApplE'
a = name.upper()
for i in a:
    print('fuits :', i)

for i in name:
    if i.isupper() :
        print(i)
    else :
        print(i.upper())

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break - 불필요한 작업을 줄여준다.(효율성과 처리속도가 좋아진다.)
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break # 브레이크 구문을 만나면 반복문을 종료한다.
    else:
        print("Not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue # 컨티뉴 이하 내용을 skip을 시켜주는 것

    print("current type : ", type(v))
    print("multiply by 2:", v * 3)

# for - else 구문 포문을 실행하고 포문을 모두 돌고나서 엘즈문을 실행
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 32:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 34...")


# 구구단 출력

for i in range(2, 10):
    for j in range(2, 10):
        print('{:4d}'.format(i * j), end='')
    print()

for i in range(2,10):
    for j in range(1,10):
        print (i,'x',j,'=',i*j)
    print()

for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i*j), end='') #print()함수 안에 쓰이는 옵션 sep='', end='', file=sys.stdout, flush 등이 있다.
    print()

# 챕터 02_01 49번째 줄
# format함수와 % 함수를 이용한 매핑('%s' -> %('one') 혹은 '{:010.3f}' -> .format('3.141592') 등을 매칭시키는 것을 의미)

# 변환 예제
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # 순서X, 중복x

