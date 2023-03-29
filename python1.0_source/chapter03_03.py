# Chapter03-3
# 파이썬 리스트 - 순서가 존재하는 시퀀스형이며, 여러가지 데이터를 담을 수 있다. (다른언어의 배열)
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O - 이러한 네 가지가 가능한 유일한 자료형)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형을 한 리스트 안에 담을 수 있다.
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안에 또다른 리스트
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱 - 원하는 데이터를 꺼내오는 과정
print('>>>>>>')
print('d - ', type(d), d) # d - <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']
print('d - ', d[1]) # d - 10000
print('d - ', d[0] + d[1] + d[1]) # d - 21000
print('d - ', d[-1]) # d - captine
print('e - ', e[-1][1]) # e - Base
print('e - ', list(e[-1][1])) # ['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3]) 
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d) # list + list => list
print('c * 3 - ', c * 3) # list * int => list

# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0])) 
# Type Error가 발생하므로 str형인 'Test'와 int형인 c[0]를 더할때는 형변환을 해서 str(c[0])를 해준다.

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[0:3])
print(c[3:0])
print()

# 같은 id 값
temp = c
print(c == temp)
print(id(temp), id(c))
print(id(temp)==id(c))
print()

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c) # c - [4, 'a', 'b', 'c', 80, 85]
c[1:2] = [['a', 'b', 'c']]
print('c - ', c) # c - [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

# 슬라이싱으로 리스트 안에 리스트를 넣으려면 대괄호를 두개 사용해야 하지만, 인덱싱 번호에 리스트를 넣으면 리스트 안에 리스트를 넣을 수 있다.
c[0] = ['a', 'b', 'c'] 
print('c - ', c) # c - [['a', 'b', 'c'], ['a', 'b', 'c'], 'b', 'c', 80, 85]

# 리스트 내용 삭제
c[1:3] = [] # 인덱스 1,2를 공백으로 수정하여 삭제
print('c - ', c)
del c[3] # 정석적인 삭제 방법 del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6) # append()함수를 이용하여 마지막에 추가
print('a - ', a)
a.sort() # 정렬
print('a - ', a)
a.reverse() # 역순
print('a - ', a)
print('a - ', a.index(5), a[5])
a.insert(2, 7) # 삽입 함수 insert(삽입할 위치, 삽입할 값)
print('a - ', a)
a.reverse()
a.remove(1) # 데이터가 많아질 경우 지우고자 하는 데이터의 인덱스 번호에 접근해서 지우기가 쉽지 않으니 값을 찾아 지워주는 remove(값) 함수를 사용한다.
print('a - ', a)
print('a - ', a.pop()) # pop() 함수 마지막 인덱스 원소를 가져오고 나머지 원소들로 리스트를 구성한다. lifo (last in first out)
print('a - ', a.pop()) 
print('a - ', a)
print('a - ', a.count(4)) # 원하는 값이 리스트 안에 몇개나 있는지 찾을때 count(값)
ex = [8, 9]
a.extend(ex) # 끝에 연장한다. 
print('a - ', a) # [a[0], a[1] ... a[n], ex[0], ex[1]]
# 삭제 remove, pop, del

a[0:1]=3,4,2
print(a)
# 반복문 활용
while a:
    l = a.pop()
    print (l)
    if 2 is l:
        print(a)
        break