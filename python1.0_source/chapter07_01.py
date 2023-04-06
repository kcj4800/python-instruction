# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다. - 증거를 남긴다. 
# 3. 예외는 던져진다. - 다른데로 처리를 위임할 수 있다.
# 4. 예외 무시 - 나쁜 습관
'''
# 예외(Exception) 개념 및 처리
 - 예외 종류
 - 다양한 예외 재연
 - 예외 처리 기본
 - 예외 처리 패턴
 - 예외 처리 실습
'''

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError

# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2()) # AttributeError: module 'time' has no attribute 'time2'. Did you mean: 'time'?

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200) - 시퀀스 자료형에서 참조하고자 하는 데이터가 없을 때 발생

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행(try - except - finally) - 자바에도 존재(try - catch - finally)

name = ['Kim', 'Lee', 'Park']

# 예제1
# try:
#     z = 'Kim' # 'Cho'
#     x = name.index(z) # name이란 시퀀스 변수에 index메소드를 사용하여 z의 인덱스를 찾는 함수를 x에 넣음.
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

print()

# 예제2

# try:
#     z = 'Cho' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except : # 모든 예외를 다 잡는다. except Exception : 으로도 쓴다.
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

print()

# 예제3

# try:
#     z = 'Cho' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e: # 에러의 내용을 출력해준다.
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else: # 예외가 발생하지 않을 경우 실행
#     print('Ok! else.')
# finally: # 예외가 발생하든 안하든 무조건 마지막에 실행
#     print('Ok! finally')

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생(예외를 던져야 하는 경우)
# 내부정책에 의해 예외를 강제로 발생시켜야 하는 경우
'''
a = 
'''
# try:
#     a = 'Park'
#     if a == 'Park':
#         print('OK! Pass!')
#     else:
#         raise ValueError
# except ValueError:
#     print('Occurred! Exception!')
# else:
#     print('Ok! else!')

# 예제5 - 출석점수를 매기는 출석부
name = ['Kim', 'Cho', 'Park', 'Lee', 'Hong', 'Ha', 'Na', 'Ma', 'Nang']
name2=dict()
for i in name:
    name2[i] = ''
print(name2)


lecture1 = ['Kim', 'Cho', 'Park', 'Ha', 'Na', 'Nang']
lecture2 = ['Cho', 'Park', 'Lee', 'Ha', 'Ma', 'Nang']
lecture3 = ['Kim', 'Cho', 'Lee', 'Hong', 'Ha', 'Na', 'Nang']

lecture = [lecture1, lecture2, lecture3]
print(lecture)
# name에 name2의 명단이 없을 경우 발생하는 VallueError를 처리해주자.
# name[1]='kim'+'+'
print(name)
a=0
for j in lecture :
    a+=1
    for i in name:
        try :
            z = name.index(i)
            x = j.index(i)
            print('{} Found it! {} in name'.format(i, z + 1))
            name2[i] += '+'
        except Exception as e:
            print(i,'is absent!', e, '!')
            name2[i] += '-'
        else :
            print('Ok!', i, 'comes here')
        finally :
            print('Next!')
    else :
        print()
        print('Ok! lecture', a, ' is over!', sep='')
        print('='*45)  
else :
    print('Great job, Everyone. That\'s it for today\'s lecture.')
    print(name2)
    print()
for i in name:
    print(i, '\'s score is ', name2[i].count('+') - name2[i].count('-'), sep='')


# name = ['Kim', 'Cho', 'Park', 'Lee', 'Hong', 'Ha', 'Na', 'Ma', 'Nang']
# name2=dict()
# for i in name:
#     name2[i] = ''
# print(name2)


# lecture1 = ['Kim', 'Cho', 'Park', 'Ha', 'Na', 'Nang']
# lecture2 = ['Cho', 'Park', 'Lee', 'Ha', 'Ma', 'Nang']
# lecture3 = ['Kim', 'Cho', 'Lee', 'Hong', 'Ha', 'Na', 'Nang']

# lecture = [lecture1, lecture2, lecture3]
# print(lecture)
# for i in name :
#     try :
#         z = name.index(i)
#         x = lecture1.index(i)
#         print('{} Found it! {} in name'.format(i, z + 1))
#         name2[i] += '+'
#     except Exception as e:
#         print(i,'is absent!', e, '!')
#         name2[i] += '-'
#     else :
#         print('Ok!', i, 'comes here')
#     finally :
#         print('Next!')

#     try :
#         z = name.index(i)
#         x = lecture2.index(i)
#         print('{} Found it! {} in name'.format(i, z + 1))
#         name2[i] += '+'
#     except Exception as e:
#         print(i,'is absent!', e, '!')
#         name2[i] += '-'
#     else :
#         print('Ok!', i, 'comes here')
#     finally :
#         print('Next!')
    
#     try :
#         z = name.index(i)
#         x = lecture3.index(i)
#         print('{} Found it! {} in name'.format(i, z + 1))
#         name2[i] += '+'
#     except Exception as e:
#         print(i,'is absent!', e, '!')
#         name2[i] += '-'
#     else :
#         print('Ok!', i, 'comes here')
#     finally :
#         print('Next!')

# else :
#     print('Ok! Today\'s lecture is end!')
#     print(name2)
# for i in name:
#     print(i, '\'s score is ', name2[i].count('+') - name2[i].count('-'), sep='')