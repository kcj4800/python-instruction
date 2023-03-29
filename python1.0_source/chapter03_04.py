# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) - 슬라이싱해서 값을 변경하거나 수정이 불가 # 불변! 중요한 데이터값 튜플로 저장!
'''
#튜플 사용법
 - 튜플 선언
 - 튜플 특징
 - 튜플 슬라이싱
 - 튜플 함수
 - 팩킹 & 언팩킹
'''
# 선언 소괄호!
a = ()
a2 = (1) # int형으로 저장되므로 뒤에 콤마를 찍어주어 튜플형으로 만들어준다.
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) # captain
print('e - ', e[-1][1]) # Base
print('e - ', list(e[-1][1])) # ['B', 'a', 's', 'e']

# 수정 X
# d[0] = 1500
# print('d - ', d)

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수 index(값) - 값의 위치가 어느 인덱스에 있는지 알수있다. count(값) - 값이 튜플 안에 몇개가 중복되는지 알수 있다.
a = (5, 2, 3, 1, 4, 5, 3, 4, 2, 4)

print('a - ', a)
print('a - ', a.index(5)) # a - 0 : 찾고자 하는 값의 인덱스 번호가 중복되면 가장 앞에있는 인덱스 번호를 알려준다.
print('a - ', a.count(4))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
y = 'foo', 'bar', 'baz', 'qux' # 괄호가 없어도 튜플로 인식해서 패킹할 수 있지만, 관습상 괄호를 사용하여 튜플임과 패킹임을 알려준다.
print(t, ':', type(t), y,':',type(y))
# 출력 확인
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t 
a1, a2, a3, a4 = t # 괄호가 없어도 튜플로 인식해서 언패킹이 되지만 관습상 괄호를 사용하여 튜플임과 언패킹임을 알려준다.
# 출력확인
print(x1)
print(x2)
print(x3)
print(x4)

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3 # 팩킹
t3 = 4, # 팩킹
x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = 4, 5, 6 # 언팩킹

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)