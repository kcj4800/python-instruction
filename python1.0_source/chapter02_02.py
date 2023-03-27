# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

'''
#오늘의 목차
다양한 변수 선언법
    - 변수 할당 설명
    - object identity
    - 변수 네이밍 규칙
    - 예약어
'''

# 기본 선언
n = 700 # n에 700이라는 정수를 할당(삽입)한다. n의 주소로 값을 할당하는 것.

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700

# 출력
print(x, y ,z) # 700 700 700

# 막간을 이용한 print 함수의 옵션 활용 (end=' ', sep=' ')
print(x, y ,z ,sep=',',end='\n') # 700,700,700
print(x, y, z, end='**')
print(x, y, z, end='\n') # 700 700 700**700 700 700

#선언
var = 75

# 출력
print(var)
print(type(var))

# 재 선언
var = "Change Value" # 재할당

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태 -> a = 300
# 1. 타입에 맞는 오브젝트 생성 -> a = int(300)
# 2. 값 생성 -> a라는 변수의 주소값에 int형 300 할당
# 3. 콘솔에 출력 -> 300

# 예1)
print(300)

# 예2)
# n -> 777
n = 777

print(n)
print(type(n)) # 777 <class 'int'>

m = n 
# a = b 의 의미는 b에 있는 것을 'a에 넣어라(할당하라)'라는 뜻이며, 
# a == b 의 의미는 'a와 b가 같냐'라는 논리값으로 True or False 값이 나온다. 
# m-> 777 <- n

print(m, n) # , 뒤에는 띄어쓰기를 하도록 문법상 권장함.
print(type(m), type(n))

m = 400
# m-> 400, 777 <-n

print(m)
print(type(m))


# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m)) # 1669175553968 -> m의 id값 즉 고유값.
print(id(n)) # 1669175554064 -> n의 id값 즉 고유값.
print(id(m) == id(n))
print()


# 같은 오브젝트 참조 -> 같은 값일때 같은 id값을 참조한다. -> 효율성

m = 800
n = 800
z = 800
i = 800

print(id(m)) # 1669175553968
print(id(n)) # 1669175553968
print(id(z)) # 1669175553968
print(id(i)) # 1669175553968
print(id(m) == id(n) == id(z) == id(i))
print()

# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates -> 주로 Method 선언시 사용
# Pascal Case :  NumberOfCollegeGraduates -> 언어를 따지지 않고 주로 Class 선언할때 사용
# Snake Case :  number_of_college_graduates -> 주로 파이썬에서 변수를 선언할때 사용

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 숫자로 시작하거 특수문자(_제외)로 시작하는 변수는 선언 할 수 없다. 1age = 9 -> Error

# 예약어(python reserved words)는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""