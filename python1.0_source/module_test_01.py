import sys
import time

print(time.time())
print(sys.path)
print(type(sys.path))

# sys.path.append('C:\\Users\\chan\python study\\python1.0_source\\math')
# # sys.path.append('C:/Users/chan/python study/python1.0_source/math') 라고 입력해도 정상적으로 경로 추가가 된다.
# print(sys.path)

# import math_test

# print(math_test.power(10, 3))

import chapter06_02

f = chapter06_02
print(chapter06_02.power(10,10))
print(f.divide(20, 5))