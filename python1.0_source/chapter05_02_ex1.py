# Chapter05-2-ex1
# 파이썬 사용자 입력
# Input 사용법(2023년 추가)
# 기본 타입(str)


# 예제1 -> 예외처리 (try - except 챕터 7에서 나옴.)
# try:
#     n = int(input('Enter a number: '))
#     print('OK. Your number is: ', n)

# except ValueError:
#     print('This is not a number.')
    

# 예제2 -> 올바른 값 입력 완료 까지 지속
# while True:
#     try:
#         n = int(input('Enter a number: '))
#         break
    
#     except ValueError:
#         print('This is not a number. Try again.')
        
# print('OK. Your number is: ', n)

while True:
    try:
        n = int(input('Enter Your Number :'))
        print('Ok, Your Number is :', n)
        break
    
    except ValueError :
        print('Oops, It is not a number. Try again')