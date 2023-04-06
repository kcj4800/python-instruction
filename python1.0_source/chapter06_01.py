# Chapter06-1
# 파이썬 클래스 - 틀
# OOP(객체 지향 프로그래밍), Self(인스턴스화된 대상 - 파이썬 코드상 메모리에 올라가는 것), 인스턴스 메소드, 인스턴스 변수

# 객체란? 소프트웨어에 우리가 구현할 대상을 객체라고 한다.
# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유 class 선언 당시 생성된 변수, 같은 클래스 내에서 공유
# 인스턴스 변수 : 객체마다 별도 존재, self를 이용하여 생성한 변수 별도로 존재 객체의 한 종류(self를 인자로 받는 것들)

# 예제1
class Dog(object): # 클래스라는 예약어로 시작! object상속 (object)는 생략 가능 class Dog: 혹은 class Dog(): 로 사용 가능
    # 클래스 속성
    species = 'firstdog'
    
    # 초기화/인스턴스 속성 - 자바의 생성자
    #파라미터 def __init__(self, name, age)의 이름은 맵핑만 잘해주면 크게 중요하지 않다. self.name 에 들어가는 이름은 호출시 사용되므로 중요하다.

    def __init__(self, name, age):
        self.name = name
        self.age = age
# 클래스는 붕어빵 틀, 인스턴스는 클래스 코드에서 사용하는 객체

# 클래스 정보
print(Dog)
print(type(Dog))

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog('왈왈이', 11)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)
print('dog3', c.__dict__)
print(Dog.__dict__)
del c # del 변수 - 선언된 변수를 삭제한다.
print('================================')
# print(c.__dict__)
print()

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) # 클래스 변수에는 클래스로도 직접 접근 가능하고,
print(a.species) # 인스턴스화된 변수에도 접근이 가능하다.
print(b.species)

# 예제2
# self의 이해
# class를 선언하고 def __init__ (self,name,age): 처럼 할수도 있지만 바로 함수를 넣을 경우 자동으로 __init__ 메소드를 내부적으로 실행해준다.
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self, num):
        print(id(self))
        print('Func2 called', num)

print(dir(SelfTest))
h = '3'
f = SelfTest()
print()
print(f.func2('멍'))
print()
# print(dir(f))
g=a
print(id(f))
# f.func1() # 예외 - func1은 매개변수가 없는데 아규먼트 하나가 넘어왔다는 에러
# self로 호출 - 인스턴스화 시켜야 한다.
# self가 없는 func1 호출은 클래스 메소드로써 바로 호출!
f.func2('멍') # self
SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f, '멍') # f = SelfTest() 이므로 id(f) = id(SelfTest)로 나온다. 
print('-----------------------------------------------------')
SelfTest.func2(g, '야옹') # func2는 파라미터(매개변수)self가 있으므로 아규먼트(인자)를 필요로 하고 이때 g = a 이므로 id(g) != id(SelfTest) 이다.
print()
print(SelfTest.func2(f, '멍') == SelfTest.func2(g, '야옹') == SelfTest.func2(h, ''))
print()
print(id(SelfTest.func2(f, '멍')),id(SelfTest.func2(g, '야옹')),id(SelfTest.func2(h, '')))
print()
print(id(SelfTest.func2(f, '멍')) == id(SelfTest.func2(g, '야옹')) == id(SelfTest.func2(h, '')))
print()
print(SelfTest.func1())
print('-----------------------------------------------------')
# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 
    stock_num = 0 # 재고
    
    def __init__(self, name): # __init__ () : init 함수는 객체가 생성될때 자동으로 호출되는 함수.
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self): # __del__ () : del 함수는 객체가 소멸할때 자동으로 호출되는 함수 
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__) # 인스턴스의 네임스페이스에서는 클래스 변수를 알수없다.
print(user2.__dict__) # 인슽턴스의 네임스페이스
print('before', Warehouse.__dict__) # 클래스의 네임스페이스에서 클래스 변수를 확인 가능하다.
print('>>>', user1.stock_num) # 모든 인스턴스에서 클래스변수를 공유한다.

user3 = Warehouse('Kim')
user4 = Warehouse('Kim')

print('Hi', Warehouse.__dict__)

del user1
print('after', Warehouse.__dict__)
print('>>>', Warehouse.stock_num)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 초기화/인스턴스 속성 
    def __init__(self, name, age, sound): # self로는 매개변수의 이름을 받고, name과 age는 받은 매개변수의 메소드로 호출된다.
        self.name = name
        self.age = age
        self.sound = sound
    
    def info(self): # info(self)에서 self는 각각의 매개변수 명이 들어간다.
        return '{} is {} years old'.format(self.name, self.age)
        
    def speak(self):
        return "{} says {}!".format(self.name, self.sound)


# 인스턴스 생성
c = Dog('july', 4, '멍멍')
d = Dog('Marry', 10, '왈왈')
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출 - speak(self, sound)에서 self로는 c와 d를 받지만 sound는 넘겨줘야한다.
# print(c.speak('Wal Wal'))
# print(d.speak('Mung Mung'))
print(c.speak())
print(d.speak())