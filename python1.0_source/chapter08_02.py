# Chapter08-2
# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, os, shutil, glob, temfile, time, random 등
'''
# 외장 함수 기본 실습
 - 외장 함수 설명
 - 중요한 외장 함수
 - 각 함수 예제 실습
 - os, sys, time 중요
'''

# sys : 실행 관련 제어
import sys

# 예제1
print(sys.argv)

# 예제2(강제 종료)
# sys.exit() - 굉장히 위험한 함수.

# 예제3(파이썬 패키지 위치) 
print(sys.path) # 현재 모든 패키지들의 위치를 표시해준다.


# pickle : 객체 파일 쓰기 - 파이썬에서 읽을 수 있는 어떠한 데이터 타입들을(객체, 클래스, 변수, 메소드 등의 코드) 파일로 쓸수 있다.
# import pickle
import pickle

# 예제4(쓰기)
f = open("test.obj", 'wb') # open(info, type) 함수로 쓰며, info 자리에는 파일에 대한 정보(파일명, 확장자), 입력 방식(wb: write, binary)
obj = {1: 'python', 2: 'study', 3: 'basic', 4: 'holy', 5: 'moly'} 
pickle.dump(obj, f) # pickle.dump 메소드로 호출하여 쓴다.
f.close() # open()함수로 열었으면 close()함수로 닫아줘야 한다.

g = open("Test2.txt", 'wb')
obj={1: 'pp', 2: 'jj', 3: 'qq'}
pickle.dump(obj, g)
g.close()

g = open("Test2.txt", 'rb')
data = pickle.load(g)
print(data, type(data))
g.close()


# 예제5(읽기)
f = open("test.obj", 'rb') 
data = pickle.load(f) # 쓸때는 pickle.dump()로 쓰고, 읽을때는 pickle.load()로 읽어준다.
print(data, type(data))
f.close() # open을 했으면 close로 닫아준다.


# os : 환경 변수, 디렉토리(파일) 처리 관련, mac, window 같은 운영체제에서 사용할 수 있는 기능들 작업 관련
# 매크로를 만들때, 업무 자동화, 카톡 실행, 게임 실행, 음악재생 등등 을 파이썬 코드로 실행 할수있게 도와준다.
# mkdir(폴더를 생성), rmdir(폴더가 비어있으면 삭제), rename(이름 바꾸기)
import os

# 예제6
print(os.environ)
print(os.environ['USERNAME'])
print(os.environ['userprofile'])

# 예제7(현재 경로)
print()
print(os.getcwd())
print(os.getcwd())

# time : 시간 관련 처리
import time

# 예제8

print(time.time()) # 1680792295.364393
print(time.time())
print(time.localtime(time.time()))
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time)))
for i range(5):
	print(i)
	time.sleep(1)


# 예제9(형태 변환)
print(time.localtime(time.time()))
# time.struct_time(tm_year=2023, tm_mon=4, tm_mday=6, tm_hour=23, tm_min=44, tm_sec=55, tm_wday=3, tm_yday=96, tm_isdst=0)

# 예제10(간단 표현)
print(time.ctime()) # Thu Apr  6 23:44:55 2023

# 예제11(형식 표현) - strftime : string format time 원하는 형식으로 출력 가능
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 2023-04-06 23:44:55

# 예제12(시간 간격 발생)
for i in range(5):
	print(i)
	time.sleep(1) # 1초 슬립


# random : 난수 리턴
import random

# 예제13
print(random.random())

# 예제14
print(random.randint(1, 45)) # 1부터 45까지 정수를 랜덤으로 호출
print(random.randrange(1,45)) # 1부터 44까지 정수를 랜덤으로 호출

# 예제15(섞기) - 데이터 분석이나 표본값을 뽑을 때, 카드 게임등에 사용
d = [1, 2, 3, 4, 5] 
random.shuffle(d)
print(d)

# 예제16(무작위 선택)
c = random.choice(d)
print(c)


# webbrowser : 본인 OS 의 웹 브라우저 실행
# 운영체제 권한 등 문제에 의해 실행 안될 가능성 있어요.
import webbrowser

# 예제17
webbrowser.open("http://google.com")

# 예제18(새창 실행)
webbrowser.open_new("http://google.com")