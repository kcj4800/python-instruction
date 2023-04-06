# Chapter06-3
# 파이썬 패키지 - 모듈을 모아놓은 폴더(06_02에서의 math 폴더 혹은 python study 폴더 등등)
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대 경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제1
# import는 파일을 받는다. 
# from sub.sub1 import module1 혹은 from sub.sub1 import * 등으로 from을 통해 폴더를 불러온 뒤 import로 파일을 열수있다.
# from 으로 열 경우에는 module1.mod1_test1()처럼 호출명이 짧아진다. 이를 변수에 담아 활용하는 것도 가능하다.
# 이때 상위 폴더에 sub파일이 존재할 경우에는 from ..sub.sub1 import * 혹은 import ..sub.sub1.module1 처럼 사용하면된다.

import sub.sub1.module1 
import sub.sub2.module2 as t # import로 불러올때부터 as를 사용하여 변수 t에 할당 할 수있다.

# import sub.sub1.module1
# import sub.sub2.module2

# import sub.sub1.module1
# import sub.sub2.module2

# 사용 - 모듈 사용시에는 sub.sub1.module1.mod1_test1()처럼 경로까지 입력해줘야한다. 이를 매개변수에 담아 활용가능하다.
a = sub.sub1.module1
a.mod1_test1()
a.mod1_test2()
print()

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

# 사용
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()
print()

print() # import로 불러올때부터 as를 사용하여 변수에 할당할 수도 있다.
t.mod2_test1()
t.mod2_test2()


print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # Alias

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()
