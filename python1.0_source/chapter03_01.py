# Chapter03-1
# 숫자형
'''
# 숫자형 사용법
    - 파이썬 모든 자료형
    - 데이터 타입 선언
    - 연산자 활용
    - 형 변환
    - 외부 모듈 사용
'''

# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스) - 시퀀스는 반복을 처리할수있고, 순서가 있다. (iterable)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입(변수가 예약어 이므로, 17라인 ~ 40라인 삭제 후 진행)
# str1 = "Python"
# bool = True or False
# str2 = "Anaconda"
# float = 10.0 # 10 == 10.0 -> False 10은 정수형(int)이고 10.0은 실수(float)형으로 타입이 다르다.
# int = 7
# list = [str1, str2]
# dict = {
#     "name": "Machine Learning",
#     "version": 2.0,
#     "용도": "학습"
# }
# tuple = 3, 5, 7 or (3, 5, 7) -> 괄호를 하는게 정석이지만 괄호가 없어도 기본적으로 튜플형이 적용된다.
# set = {7, 8, 9}

# # 데이터 타입 출력
# print(type(str1))
# print(type(bool))
# print(type(str2))
# print(type(bool))
# print(type(float))
# print(type(int))
# print(type(dict))
# print(type(tuple))
# print(type(set))
# print(type(str1))
# print(type(str2))

# 숫자형 연산자
"""
+ 
- 
* 
/ : 나누기
// : 몫 
% : 나머지
divmod : 몫 과 나머지로 반환
abs(x) : 절대값 
int(x) 
float(x) 
complex(x) : 복소수
pow(x, y) : 제곱 
x ** y : 제곱
true : 1
false : 0
....
"""

# 정수 선언
i = 77
i2 = -14
big_int = 999999999999999999999999999999999999999
# 자바나 다른언어 사용시 이렇게 큰 수는 bigint 등 다른 식으로 처리해야 하지만 파이썬은 자동으로 해준다.

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 

# -
print(">>>>> -")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)

# *
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)

# /
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)

# //
print(">>>>> //")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)

# %
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)

# **
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)

# 형 변환 실습
a = 3. # 3.0을 의미하며 0은 생략 가능
b = 6
c = .7 # 0.7을 의미하며 0은 생략 가능
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환 
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수로 바뀌면서 소숫점 이하의 수는 버림. 12.7 -> 12
print(int(True))  # Bool -> 정수 -> 1
print(float(True))  # Bool -> 정수 -> 1.0
print(int(False))  # Bool -> 정수 -> 0
print(float(False))  # Bool -> 정수 -> 0.0
print(complex(3))  # 정수 -> 복소수 -> 3+0j
print(complex('3'))  # 문자 -> 복소수 -> 3+0j 
print(complex(False))  # Bool -> 복소수 -> 0+0j

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 몫과 나머지를 반환하는 함수 divmod(나누어지는 수(피제수), 나누는 수(제수))
print(x, y)
print(pow(5, 3), 5 ** 3)

#외부 모듈
import math

#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수

#floor

#pi
print(math.pi)
