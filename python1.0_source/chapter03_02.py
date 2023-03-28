# Chapter03-2
# 파이썬 문자형
# 문자형 중요
'''
# 문자형 사용법
    - 문자형 중요성
    - 문자형 출력
    - 이스케이프, rawstring은 이스케이프(\)를 무시한다.
    - 멀티 라인
    - 문자형 연산
    - 문자형 형 변환
    - 인덱싱
    - 문자열 함수
    - 슬라이싱
'''
# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print(type(str1), type(str2), type(str3), type(str4))
print()

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str_t1 = ''
str_t2 = str() # 좀더 정석적인 방법.

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
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

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'


# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String -> 보통 경로를 지정해줄 때 사용하며, 맥, win, 리눅스 등 os에 따라 슬러시 기호가 다르기 때문에 raw string을 사용한다.
raw_s1 = r'D:\Python\python3' 
raw_s2 = r"\\x\y\z\q"


# Raw String 출력
print(raw_s1)
print(raw_s2)

# 멀티라인 입력 # 변수 선언시 \로 끝나면 뒤에 어떤 변수를 바인딩 한다라는 의미.
multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """
a9 = \
'고구마' \
'튀김' \
'맛이쪙'

print(a9) # 고구마튀김맛이쪙

b9 = \
'감자' \
'튀김' \
'맛이쪙'\

print(b9) # 감자튀김맛이쪙

# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(3 * str_o1 * 3)
print(str_o1 + str_o2)
print(dir(str_o1))
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2) # 대문자 'P'가 str_o2안에 없니?

# 문자열 형 변환
print(str(66),type(66))  # type 확인
print(str(10.1))
print(str(True), type(str(True)))
print(str(complex(12)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha 등)
print("Capitalize: ", str_o1.capitalize()) # 대문자로 바꿔주는 함수 Capitalize()
print("endswith?: ", str_o2.endswith("s")) # 끝글자가 뭘로 끝나는지를 확인 할수 있는 endswith() 함수.
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('thon', ' Good')) # 찾아바꾸기 replace(a, b)
print("replace2: ", str_o3.replace("are", "was")) # 리스트 형태로 반환해주는 오름차순 정렬!
print("split: ", str_o4.split(' '), type(str_o4.split(' '))) # 반복되는 구분기호(띄어쓰기, 콤마 등)를 이용하여 리스트 형태로 반환(언패킹)
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_sl = 'Nice Python'

# 슬라이싱 연습 -> 대괄호를 이용하여 인덱스를 입력한다.
print(str_sl[0:3]) # 0,1,2 출력
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:9:2]) # 인덱스 1부터 9-1까지 2칸씩 출력
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::-1]) # 처음부터 끝까지 가져오되 역순으로 가져오세요.
print(str_sl[::2]) # 처음부터 끝까지 가져오되 두칸씩 건너뛰면서 가져오세요.


# 아스키코드(또는 유니코드)
a = 'z'

print(ord(a))
print(chr(122))
