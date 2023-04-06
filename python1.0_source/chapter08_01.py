# Chapter08-1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)
print(all([1,2,3])) # and
print(all([1,2,0])) # false
print(all([1,2,'']))# false
print(any([1,2,0])) # or
print(any([0,'',])) # false

# chr : 아스키 -> 문자 , ord(ordinal value): 문자 -> 아스키
print(chr(122))
print(chr)
print(ord('z'))
print(chr(67))
print(ord('C'))
aaa = (['마낭이', '돼지', '꿀꿀', '고구마', '맛탕', '마시쪙', '아이스 아메리카노'])
aa=[]
# enumerate : 인덱스 + Iterable 객체 생성
aaaa=dict()
zzz=aaaa
for i, name in enumerate(aaa):
    print(str(int(i)+1)+'번', name)
    zzz[str(i+1)+'번'] = name
    # aaaa.update(str(int(i)+1)+'번' = name)
    aa.append((str(int(i)+1)+'번', name))
print(aa)

print(zzz)
for k, v in aa:
    aaaa[k]=v
print(aaaa)

print(id(aaaa),id(zzz), id(aaaa)==id(zzz),aaaa==zzz)

print('=='*30)
print()

#  filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출 필터함수
# filter(func, iter) : filter함수에 들어가는 func의 참조건에 맞는 데이터만 걸러준다. => 리스트로 형변환하여 사용한다.

def conv_pos(x):
    return abs(x) > 2
    
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

def ccc(x):
    return len(x)>=3

print()
print(ccc('고구마 맛탕'), ccc('돼지'))

print()
print('++'*22)
print(list(filter(ccc, aaa)))
print(list(filter(lambda x:len(x)>=3, aaa)))
print('+'*45)
print()
# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# max, min : 최대값, 최소값

print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
    
print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x:abs(x),[1,-3,2,0,-5,6])))

print()
def coco(x):
    if len(x)>=3:
        return len(x)
    else:
        return -len(x)
print(list(map(coco, aaa)))
print()

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림

print(round(6.5781, 2))
print(round(5.6))

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환  - tuple, list, dict, set
# 선택정렬, 삽입정렬, 퀵정렬, 병합정렬, 버블정렬 등등
# para.sort() 와 print(list(sorted(para))의 차이 리스트 정렬 후 유지 여부
# para.reverse() 와 print(list(reversed(para)))의 차이 리스트 역정렬 후 유지 여부
print()
print(')('*30)
print(aa)
aa.reverse()
print(aa)
aa.sort()
print(aa)
print()
print(list(reversed(aa)))
print(aa)
print()
aa.reverse()
print(aa)
print()
print(list(sorted(aa)))
print(aa)
print(')('*30)
print()

print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))



# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# type : 자료형 확인

print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(aa, '\n', aaa, sep='')
print(list(zip([10,20,30], [40,50,777]))) # [(10, 40), (20, 50), (30, 777)]
print(list(zip([10,20,30], [40,50]))) # [(10, 40), (20, 50)] 짝이 맞는 것 까지만 묶어준다.
print(list(zip(sorted(aa),aaa))) # len(aa) = len(aaa) = 7 이므로 리스트 안에 7개의 튜플로 묶어준다.
aaa.append('감자탕')
print(len(aa), len(aaa), '\n', list(zip(sorted(aa),aaa))) 
# 감자탕을 추가하여 len(aa)=7, len(aaa)=8 이므로 앞에서부터 7개의 쌍만 리스트 안에 튜플로 묶어준다.
print(type(list(zip([10,20,30],[40,50,777]))[0]))
# 리스트 [(10, 40), (20, 50), (30, 777)]의 0번째 원소의 타입을 물어봤으므로 <class 'tuple'>을 반환해준다.