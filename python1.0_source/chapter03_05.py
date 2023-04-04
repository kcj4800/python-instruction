# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O) - Jason과 비슷 최신 파이썬에서는 순서가 존재한다. java에서의 맵과 같다.
'''
# 딕셔너리 사용법
 - 딕셔너리 선언
 - 딕셔너리 특징
 - 딕셔너리 수정
 - 딕셔너리 함수
 - 딕셔너리 중요성
'''

# 선언 (키 : 값)
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
a1 = {'name':'Kim', 'phone': '01025114800', 'birth': '921208'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}
c1 = {'arr': [1, 2, 3, 4, 'a']}
print(c1) 
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
d1={
    'Name':'CahnJung',
    'Age':'32',
    'Grade':'B+',
    'Status':True
    
}
e =  dict([
	 ('Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)
f1=dict(
    Name='Kim',
    Grade='B+',
    Age='32',
    City='JeonJu'

)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print('f1 - ', type(f1), f1)
print()
print('#################################################################################')


# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))
print('f1 - ', f1['Name'], f1.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이 - len(딕셔너리)키의 갯수를 샌다.
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print(dir(a)) # - __iter__
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print('a - ', a.items()) # items() - 리스트형으로 보여주며 키와 밸류값을 튜플형태로 보여준다.
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('----------------------------------------------------------------------------------------')
print('a - ', list(a.items())) # 마찬가지로 리스트 안에 키와 밸류값이 튜플 형태로 저장되어있다.
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print('a - ', a.pop('name')) # pop(키값) - 키값에 맞는 밸류 값을 불러오고 딕셔너리에서 삭제한다.
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('d - ', d.pop('City'))

print('f - ', f.popitem()) # popitem() - 맨뒤에서 부터 키값과 밸류값을 함께 불러오고 딕셔너리에서 삭제한다.
print(f)
print('f - ', f.popitem())
print(f)
print('f - ', f.popitem())
print(f)
print('f - ', f.popitem())
print(f)
print('f - ', f.popitem())
print(f)
# 예외
# print('f - ', f.popitem()) # 딕셔너리 안에 값이 없을때 popitem()으로 불러오려 하면 KeyError가 발생한다.

print('a - ', 'name' in a) # a in b 연산자 -> a가 b에 있니? 딕셔너리이므로 키값을 포함하고 있는지 여부로 판단 -> True or False 
print('a - ', 'addr' in a)
print()
print('================================================================================')
print()
# 수정 & 추가
f['test'] = 'test_dict' # 추가
print(f)
f['test'] = 'dict_test' # 수정
print(f)

f.update(Age=36) # update(키=밸류)를 이용하여 추가 가능하다.

temp = {'Age': 27} # temp라는 변수에 딕셔너리를 선언해서 update(temp)로 추가/수정 할 수도 있다.

print('f - ', f)

f.update(temp)

print('f - ', f)

# dict 메소드
a = {
    '돼지' : '꿀꿀',
    '강아지' : '멍멍',
    '토끼' : '깡총',
    '병아리' : '삐약'
}
b = dict(
    말 = '히이잉',
    소 = '음모',
    닭 = '꼬끼오',
    양 = '메에',
    토끼 = '깡총깡총'
)

print(a, b)
print(a['돼지'], a.get('돼지')) # a['돼지']와 a.get('돼지')는 똑같이 키값으로 밸류값을 호출하지만 .get()메소드를 사용하는게 예외처리에 유리 
a['돼지']='꿀꿀꿀' # 추가, 수정 하나씩 가능
a.update(꿀돼지='꿀꿀꿀꿀', 돼지='꿀꿀') # update로 추가, 수정 동시에 가능, 또한 다른 dict를 추가할수도있다.
a.update(b) # .update()로 다른 dict를 추가할 수 있으며, 키값 중복시에는 수정 적용이 된다.
print(a)

# .keys(), .values(), .items()는 dict 안에 키값, 밸류값, 키와 밸류값을 불러온다.  
# .pop('값') 키에서 값을 찾아 그 밸류를값을 반환한 뒤 삭제. 불러올 키값이 없다면 에러
# .popitem() 맨 뒤에 있는 키값과 밸류값을 반환한 뒤 삭제. 불러올 키값이 없다면 에러 
print(a.keys(), a.values(), a.items(), a.pop('돼지'), a.popitem()) 
# print(a.pop('캥거루')) - KeyError
print(a)

# in 연산자로 키값을 검색하여 bool 형식으로 반환
print('돼지' in a, type('돼지' in a))
print('토끼' in a)

