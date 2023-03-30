# Chapter03-6
# 집합(Sets) 특징 - 공집합 차집합 합집합 교집합 등등
# 선형대수학, 넘파이나 싸이파이등 공학자를 위한 파이썬 사용시 쓰임.
# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a, 2 in a)
print('b - ', type(b), b, 3 in b)
print('c - ', type(c), c, 'pen' in c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 ', s1 & s2)
print('s1 & s2 ', s1.intersection(s2))

print('s1 | s2 ', s1 | s2)
print('s1 | s2 ', s1.union(s2))

print('s1 - s2 ', s1 - s2)
print('s1 - s2 ', s1.difference(s2))

# 중복 원소 확인
print('s1.isdisjoint(s2) ', s1.isdisjoint(s2))

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1이 s2의 부분집합이니?
print('superset : ', s1.issuperset(s2)) # s1이 s2를 포함하니?
print()
print('===========================================================================')
print()

# 추가 & 제거 - list (append, insert, a[0] = b - 인덱스에 접근, update(dict))
s1 = set([1, 2, 3, 4])
s1.add(5) # set에서는 add(값) 메소드로 추가하고 remove(값) 메소드로 지운다. discard(값)으로 지우면 값이 없어도 에러가 발생하지 않는다.
s1.add(3)
s1.update('업데이트 메소드로는 숫자를 넣을 수 없으며, 업데이트로 문자 입력시 한글자씩 중복과 순서가 없이 랜덤으로 출력된다.')
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)

#s1.discard(7)

# 모두 제거
print(s1)
s1.clear() # 리스트에서도 사용 가능
print(s1)
l1 = [1, 2, 3, 4, 5, 6, 7]
print(l1)
l1.clear()
print(l1)
d1 = dict(
    홀리 = '몰리',
    과카 = '몰리',
    롤리 = '폴리',
    보도 = '콜리',
    모노 = '폴리',
    로보카 = '폴리'
)
d2 = {
    '홀리' : '몰리',
    '과카' : '몰리',
    '롤리' : '폴리',
    '보도' : '콜리',
    '모노' : '폴리',
    '로보카' : '폴리'
}
print(d1, d2)
