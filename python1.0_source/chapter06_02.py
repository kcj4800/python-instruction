# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
'''
# 모듈 개념
 - 모듈이란?
 - 모듈 생성
 - sys.path 실습
 - if __name__ == '__main__': 에 대한 설명
 - 모듈 사용 실습
'''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y
    
def power(x, y):
    return x ** y
    
    
# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

# __name__ 사용 - 외부 모듈 사용시 의미 없는 것들(테스트 출력)이 출력되는 것을 막기 위한 장치(실행하는 위치가 메인일 경우에만 실행된다.)
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15)