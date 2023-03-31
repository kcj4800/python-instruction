# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

'''
# 파이썬 함수 사용법
 - 함수 중요성
 - 함수 선언 및 사용
 - 다양한 리턴 사용
 - 중첩 함수
 - 함수 Hint
 - 기타 사용법
 - 람다(Lambda) 개념
'''

# 함수 정의 방법
# def function_name(parameter): parameter =  매개변수
#     code

# 예제1
def first_func(w1):
    print("Hello, ", w1)

word = "Goodboy"

first_func(word) # first_func(word)에서 word는 arguement(인자)라고 하며, 함수를 정의할때 넣은 w1은 parameter(매개변수)라고 한다.

# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)
    

# 예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y ,z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(30)

print(type(p), p, set(p))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul3(30)
print(type(d), d, d['v1'],d.get('v2'), d.items(), d.keys()) 
# dict 타입에서 dict['key']로 호출할 경우 에러가 날수있지만, dict.get()으로 키값을 불러올경우 키값이 존재하지 않아도 에러가 나지 않는다.
print()

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 명 자유 - 
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

# *args라고 하면 여러 데이터가 팩킹 된 자료가 넘어와도 여러개의 파라미터를 생성할 필요없이 하나의 파라미터(*args)로 언팩킹하여 받겠다는 뜻이다.
# enumerate(iter) - 입력되는 iterable한 자료를 풀어서 인덱싱하여 i = 인덱싱 번호, v = 언팩킹된 자료로 반환해준다. 
def args_func2(*args):
    for i, v in enumerate(args): 
        print('번호 : ', i + 1,'이름 :', v)
    print('------------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
args_func2('Lee', 'Kim', 'Park', 'Yong', 'Holy')

# **kwargs - 딕셔너리 자료형 언팩킹은 ** 별 두개를 사용한다.
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

def kwargs_func2(**kwargs):
    for v in kwargs.keys():
        print(v, kwargs[v])
    print('-------------------')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')
kwargs_func2(name1='Lee', name2='Kim', name3='Hong', name4='Ha')
kkk = {'홀리' : '몰리',
    '과카' : '몰리',
    '롤리' : '폴리',
    '보도' : '콜리',
    '모노' : '폴리',
    '로보카' : '폴리'
}


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(str(args_1) + str(args_2))
    for i, v in enumerate(args):
        print(i+1,'번', v,sep=' ',end='  ,')
    print(' 등등')
    for v in kwargs.keys():
        print(v,'하면', kwargs[v])
    print('===== END ======')



example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)
example(10, '돼지', 'leeee', 111111111, 30303030,30,30, '코딱지', 킁가='돼지', 어흥='호랑이', 족발='맛나')

# 파라미터(매개변수)에 넣을 인수(아규먼트)를 묶어서 넣을 수는 없을까??

# 중첩함수
# 함수 안에 있는 자식 함수는 부모 함수를 호출 하지 않고선 바로 호출이 불가능하다.
def nested_func(num, num2):
    def func_in_func(num, num2):
        print(num - 100,'is', num2/num)
    print("In func")
    func_in_func(num + 100, num2*4)

nested_func(100, 203)

# 실행불가
# func_in_func(1000, 1080)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 영역에 저장 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x, y):
#    return x * y
    
#lambda x, y:x*y

# 일반적함수 -> 할당
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 10))

func_final(10, 20, lambda_mul_func)
func_final(10, 20, mul_func_var)
func_final(10, 20, lambda x,y : x*y)
func_final(10, 20, lambda x,y : x**y)

# Hint - 함수를 지정된 타입으로 생성하고 형변환등을 하여 연산에 사용 하는 예시
def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)

def tot_length3(word: str, num: float) -> None:
    return word + ' 비밀번호는 ' + str(len(word)+num*3)

def print_function(Holy):
    print(Holy, '입니당',sep=' ')

print_function(tot_length3('Hello Everyone! Welcome to ChanJung\'s House', 213))