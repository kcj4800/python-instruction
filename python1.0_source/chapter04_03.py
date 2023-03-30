# Chapter04-3
# 파이썬 반복문
# While 실습
'''
# While 흐름 제어 실습
 - While 기본 사용법
 - Break, Continue
 - While - Else 구문
 - 무한 반복 구문
 - 기본 패턴 실습
'''

# while <expr>: => if <expr>: 과 같지만 expr이 false가 될때까지 반복
#    <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1
    
# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# if 중첩
# 예제3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')  
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')   


# 예제5
i = 1

while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1


# While - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == -1:
        break
else:
    print('else out.')

# 예제7 
a = ['foo', 'bar', 'baz', 'qux', 'fow', 'rew', 'als']
s = 'rew'

i = 0

while i < len(a):
    if a[i] == s:
        print(s,'is', i+1,'th')
        break
    i += 1
else:
    print(s, 'not found in list.')
    
    
# 무한반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())








