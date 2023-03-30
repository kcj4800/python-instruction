# Chapter04-1
# 파이썬 제어문
# IF 실습
'''
# IF 구문 실습 - 모든 언어에 존재하며, MySQL, Oracle 등 subquery에도 존재한다.
 - 관계 연산자 실습
 - 논리 연산자 실습
 - 일반 조건문
 - 다중 조건문
 - 중첩 조건문
'''
# 기본 형식

print(type(True)) # bool 형식이 중요함. 0이 아닌 수, 문자열, "abc" , [1,2,3], (1,2,3)...
print(type(False)) # 0, "", [], (), {}...

# 예1 if 조건식 :
if True:
    print("Good")  # 들여쓰기(Indent)

if False:
    # 실행 X
    print("Bad")

# 예2
if False:
    # 여기는 실행되지 않음.
    print("Bad")
else:
    # 여기가 실행된다.
    print("Good")

# 관계연산자 종류
# >, >=, <, <=, ==, !=


x = 15
y = 10

# == 양 변이 같을 때 참.
print(x == y)

# != 양 변이 다를 때 참. 
print(x != y)

# > 왼쪽이 클때 참.
print(x > y)

# >= 왼쪽이 크거나 같을 때 참.
print(x >= y)

# < 오른쪽이 클 때 참.
print(x < y)

# <= 오른쪽이 크거나 같을 때 참.
print(x <= y)

# 참 거짓 판별 종류
# 참 : "values", [values], (values), {values}, 1
# 거짓 : "", [], (), {}, 0, None

city = ""
if city:
    print("You are in:", city)
else:
    # 출력
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    # 출력
    print("Please enter your city")

# 논리연산자(중요)
# and, or, not
# 참고 : https://www.tutorialspoint.com/python/python_basic_operators.htm

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)  # a > b > c
print('or : ', a > b or b > c) # 만약에 앞의 연산에서 이미 True가 나온다면 뒤에 연산은 하지 않는다. 효율성!
print('not : ', not a > b)
print('not : ', not b > c)
print(not True) # False
print(not False) # True

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용 # 산술(숫자 계산을 먼저한 뒤) 관계 (크거나 같은지)를 따진다음 논리(and, or, not)를 연산한다.

print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10) # True and not True 이므로 True and False => False

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
    print("Pass.") # indent를 안하면 에러가 난다. tab or 띄어쓰기 4번
else:
    print("Fail.")

# 예제

id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin":
    print("관리자 인증")

if id2 == "admin" and grade == "platinum":
    print("최상위 관리자")


# 다중 조건문
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80: # else의 경우 위에 조건이 아니라면 이라는 뜻이지만 elif를 이용하면 또 다른 조건 제시 가능
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')
b1=[]
# 중첩 조건문
name = ['김', '박', '돼지', '말', '소', '히이잉','가자미','고구마','무지개','가마니','기마낭','임금님']
grade = ['A','B','C','A','D','B','A','C','D','B','A','A']
total = [95, 90, 80, 50, 60, 90, 90, 80, 90, 100, 95, 100]
for i in range(0, len(name)) :
    temp = {
        'name' : name[i],
        'grade' : grade[i],
        'total' : total[i] 
    }
    b1.append(list(temp.values()))

print(b1)
print()
print('=============================================================================')

for i in range(0, len(b1)) :
    if b1[i][1] == 'A' :
        if b1[i][2] >= 90 :
            print(b1[i][0], ': 장학금 100%')
        elif b1[i][2] >= 80 :
            print(b1[i][0], ': 장학금 80%')
        elif b1[i][2] >= 70 :
            print(b1[i][0], ': 장학금 50%')
        else :
            print(b1[i][0], ': 장학금 30%')
    elif b1[i][1] == 'B' :
        if b1[i][2] >= 90 :
            print(b1[i][0], ': 장학금 70%')
        elif b1[i][2] >= 80 :
            print(b1[i][0], ': 장학금 40%')
        elif b1[i][2] >= 70 :
            print(b1[i][0], ': 장학금 20%')
        else :
            print(b1[i][0], ': 장학금 없음')
    else :
        print(b1[i][0], ': 장학금 없음')

print()
print('=================================================================')
print()

print(type(a))
# for i in name :
#     a={'name' : i}
#     for j in grade :
#         a={'grade' : j}
#         for k in total :
#             a={'total' : k}
# 출석부[]
# if grade == 'A':
#     if total >= 90:
#         print("장학금 100%")
#     elif total >= 80:
#         print("장학금 80%")
#     else:
#         print("장학금 70%")
# else:
#     print("장학금 50%")

if grade == 'A':
    if total >= 90 :
        print('장학금 100%')
    elif total >= 80 :
        print('장학금 80%')
    elif total >= 70 :
        print('장학금 60%')
    else :
        print('장학금 50%')
elif grade == 'B':
    if total >= 90 :
        print('장학금 50%')
    else :
        print('장학금 30%')
else :
    print('장학금 없음')    
# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색
