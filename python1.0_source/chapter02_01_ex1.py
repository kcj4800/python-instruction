# Chapter02-1-ex1
# 파이썬 완전 기초
# Print 사용법(2023년 추가)
# 참조 : https://realpython.com/python-f-strings/
# 파이썬 3가지 Print Formatting
# 자주 나오는 질문 참고

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
### 3가지 Format Practices

#변수선언
x = 50
y = 100
text = 308276567
n = 'Lee'


'''
def sum(x, y):  #파라미터(매개변수) - 가변값
    return x + y


sum(3, 6)   # 아큐먼트(인자) - 고정값



map객체 주소값

N, M = map(int, (3,5))
map()함수를 print하게되면 그 객체의 주솟값이 나오므로 항상 우리가 알수 있게 list(map())을 이용하여 형변환 해준다.

# 패킹 / 언패킹
 -> 박싱 / 언박싱

A = N, M -> A라는 변수를 선언하고 N, M의 매개변수를 담아서 팩킹해준다.

N = 3 -> N과 M 안에 인자를 넣어주며 언패킹해준다.
M = 5

swap - 파이썬에서만 가능하며, 선언된 변수들을 서로 트레이드 시킬 수 있다. 다른 언어로 이 기능을 하기 위해서는 조금 더 복잡하다.
A = 3
B = 5

A라는 값에 5, B라는 값에 3
A, B = B, A
'''

# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y)) # ' %s, %s, %d ' -> % (n, text, (x + y) )
print(ex1)


# 출력2
ex = 'n = {}, s = {}, sum={}'.format(n, text, x + y) #{}안에 인수를 넣으려면 다같이 넣거나 다같이 빼야한다.
print(ex)

ex2 = 'n = {n}, s = {srialno}, sum={sum}'.format(n=n, srialno=text, sum=x + y) 
# '{n}, {serialno}, {sum}' -> .format(n=n, serialno=text, sum=x+y)
print(ex2)


# 출력3 fstring
ex3 = f'n = {n}, s = {text}, sum={x + y}' 
print(ex3)
print(f'n={n}, s={text}, sum={x+y}')

print()
print()


# 출력4(다양한 f-string 연습)

# 진수
# (2진수 : b, 8진수 : o, 16진수 : x|X)
k = 98

print(f"k 2진수: {k:b}, k 8진수: {k:o}")
print(f"k 16진수 - l:{k:x}, U:{k:X}")

print()
print()


# 구분기호
m = 10000000000

print(f"m: {m:,}") # m을 표시할건데 ,를 넣어서 표현하여라 -> m: 10,000,000,000
print(f'{m:,}') # 10,000,000,000

print()
print()


# 정렬 : 화살표가 가리키는 방향대로 정렬 ^(위) : 가운데, >(오른쪽) : 오른쪽 정렬, <(왼쪽) : 왼쪽 정렬
# ^ : 가운데 , < : 왼쪽 , > : 오른쪽
t = 20

print(f"t :{t:10}") # t :         20 -> 10자리를 생성하고, t를 오른쪽 정렬. 그리고 나머지는 공백으로 처리
print(f"t center: {t:_^10}") # t center:     20     -> 10자리를 생성하고 t를 가운데 정렬. 그리고 나머지는 _로 처리.
print(f"t left: {t:#<10}" ) # t left: 20######## -> 10자리를 생성하고 t를 왼쪽 정렬. 그리고 나머지는 #으로 처리.
print(f"t right: {t:0>10}") # t right: 0000000020 -> 10자리를 생성하고 t를 오른쪽 정렬. 그리고 나머지는 0으로 처리.

print()
print()


# 채우기
print(f"t:{t:-^10}") # t:----20----
print(f"t:{t:#^10}") # t:####20####
print(f"t:{t:*<10}") # t:20********


#응용
z = 20000000000
print(f'z : {z:_>20,}') # z : ______20,000,000,000 -> 20자리를 만들고 z를 ,로 나누고, 오른쪽 정렬한 뒤 나머지를 _로 채움. 