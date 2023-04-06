import sys
import inspect
# from ..sub2 import module2

# module2.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe())) 
	# 실행프레임(currentframe())의 현재 파일을 조사하다(inspect).(현재경로를 보여주는 함수(inspect)의 메소드(getfile, currentframe))

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))