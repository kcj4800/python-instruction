# # Chapter05-2
# # 파이썬 사용자 입력
# # Input 사용법
# # 기본 타입(str)
# '''
# # Input 사용법
#  - 사용자 입력
#  - 형 변환 입력
#  - 입출력 실습
# '''

# # 예제1
# name = input("Enter Your Name : ")
# grade = input("Enter Your Grade : ")
# company = input("Enter Your Company name : ")

# print(name, grade, company)

# # 예제2
# number = input("Enter number : ")
# name = input("Enter name : ")

# print("type of number", type(number), number * 3)
# print("type of nanme", type(name))

# # 예제3(계산) - 형변환 - input() 함수는 str 형으로 받기 때문에 숫자로써 받기 위해서는 int()혹은 float()형으로 형변환 해줘야 한다.
# first_number = int(input("Enter number1 : "))
# second_number = int(input("Enter number2 : "))

# total = first_number + second_number
# print("first_number + second_number : ", total)


# # 예제4
# float_number = float(input("Enter a float number : "))

# print("input float : ", float_number)
# print("input type : ", type(float_number))


# 예제5 -> fstring - print(f'{}, {}'), format함수 - print({0},{1}.format(x, y))
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))
x=input('Enter your first name : ')
y=input('Enter your last name : ')
print(f'Firstname : {x}, lastname : {y}')