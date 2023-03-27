# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력 print함수에는 sep, end, file, flush 등의 옵션이 있다.
print('Python Start!') # print 함수의 괄호 안에 넣는 것을 인수 즉 파라미터라고 한다.
print("Python Start!") # print 함수 안에 문자를 입력할때는 ' ', " ", ''' ''', """ """ 등의 방법이 있다. 
print("""Python Start!""")
print('''Python Start!''')

print() # print 함수 안에 인수를 넣지 않고 공백으로 두면 줄바꿈이 된다. escape 라는 것도 있다.

# separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N', sep='') #sep라는 옵션은 어떤식으로 분리가 될지를 정해준다.
print('010', '7777', '7777', sep='-') # 010-7777-7777
print('python', 'google.com', sep='@')# python@google.com

print()

# end 옵션 사용
print('Welcome To', end=' ') #end 옵션은 끝부분 처리를 어떻게 할것인지를 결정
print('IT News', end=' ')
print('Web Site') # Welcom To IT News Web Site

print()

# file 옵션 사용
import sys #import는 예약어로써 변수로 선언이 불가능하다.

print('Learn Python', file=sys.stdout) #file 옵션을 이용하여 콘솔아웃을 의미

print()

#flush 옵션이라는 것도 있다.

# format 사용(d : 정수(digit), s : 문자열(string), f : 실수(float)) 
print('%s %s' % ('one', 'two')) # one two -> 좀더 정석적
print('{} {}'.format('one', 'two')) # one two -> format이 좀더 유연하게 사용가능
print('{1} {0}'.format('one', 'two')) # two one -> 인덱스 안의 순서에 따라 입력된다.

# %s
print('%10s' % ('nice',)) #      nice : 총 열개의 자리를 차지하고 왼쪽부터 공백을 채우고 nice를 채움 
print('{:>10}'.format('nice')) #      nice : 같은 표현

print('%-10s' % ('nice',)) #nice      : 총 열개의 자리를 차지하고 nice를 왼쪽부터 채운 뒤 나머지 공백
print('{:10}'.format('nice')) #nice      : 같은 표현

print('{:_<10}'.format('nice')) #nice______ : 총 열개의 자리를 차지하고 왼쪽부터 nice를 채운 뒤 나머지를 _로 처리 화살표가 가리키는 방향부터 문자를 채운다.
print('{:_>10}'.format('nice')) #______nice : 총 열개의 자리를 차지하고 오른쪽부터 nice를 채운뒤 나머지를 _로 처리
print('{:^10}'.format('nice')) #   nice   : 총 열개의 자리를 차지하고 nice를 가운데에 채운뒤 나머지 공백처리
print('{:_^10}'.format('nice')) #___nice___ : 총 열개의 자리를 차지하고 nice를 가운데에 채운뒤 나머지를 _로 처리

print('%5s' % ('pythonstudy',)) # pythonstudy : 5자리를 생성하지만 글자가 그 이상이라면 그 만큼 다 표시
print('%.5s' % ('pythonstudy',)) # pytho : 5자리를 생성하고 그 이상의 문자는 절삭
print('{:.5}'.format('pythonstudy')) # pytho
print('{:10.5}'.format('pythonstudy')) # pytho : 10개의 공간을 생성하지만 5자리 이상의 문자는 절삭

print()

#예제
print('{:_>10.7s}'.format('pythonstudy')) # ___pythons : 10자리를 생성 후 오른쪽부터 7자리까지만 표현 후 나머지는 _로 처리.

# %d - 정수 출력
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%04d' % (42,)) # 4자리를 갖고 정수부를 그대로 표현 나머지는 0으로 채운다.
print('{:4d}'.format(4212344))

# %f
print('%f' % (3.141592653589793,)) # 정수부는 그대로 표현, 소숫점은 기본값인 6자리까지만 표현 나머지 절삭.
print('{:f}'.format(3.141592653589793)) # 정수부는 그대로 표현, 소숫점은 기본값인 6자리까지만 표현 나머지는 절삭.

print()

print('%06.2f' % (3.141592653589793,)) # 6자리를 갖고 정수는 그대로 표현, 소숫점은 2자리까지만 표현하고 절삭, 나머지는 0으로 채운다.
print('%010f' % (3.141592653)) # 10자리를 갖고, 정수는 그대로 표현, 소숫점은 기본값인 6자리까지만 표현하고 절삭, 나머지는 0으로 채운다. 

print()

print('{:06.3f}'.format(3.141592653589793)) # 6자리를 갖고 정수는 그대로 표현, 소숫점은 3자리까지 반올림으로 표현하고 절삭, 나머지는 0으로 채운다.
print('{:010.2f}'.format(3.141592653)) # 10자리를 갖고 정수는 그대로 표현, 소숫점은 2자리까지 반올림으로 표현하고 절삭. 나머지는 0으로 채운다.
print('{:06.3f}'.format(3.141592653)) # 6자리를 갖고 정수는 그대로 표현, 소숫점은 3자리까지만 반올림으로 표현하고 나머지 절삭, 나머지 자리는 0으로 채운다. 
print('{:010f}'.format(3.141592653)) # 10자리를 갖고 정수는 그대로 표현, 소숫점은 기본값인 6자리까지 반올림으로 표현 나머지는 0으로 채운다. 

print()
#예제연습
print('{:10.3f} {:010.3f}'.format(3.141592653, 3.141592653)) #      3.142 0000003.142
print('{:010.3f}***{:10.3f}'.format(3.141592653, 3.141592653)) #0000003.142***      3.142

