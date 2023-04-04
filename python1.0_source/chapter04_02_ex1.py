# 오늘의 로또!
import random
a=[]
for i in range(1, 46):
    a.append(i)

print(a)

for i in range(0,6) :
    random.shuffle(a)
    print('오늘의 로또', i+1, '번째 숫자는 :', a.pop())

# 랜덤함수
'''
기본적으로 랜덤함수는 random 모듈을 import로 불러와서 사용한다.
random.random() - 0 ~ 1까지의 난수를 반환
random.randrange(1,46,2) - 0부터 45까지 2씩 건너뛰면서 범위를 갖고 그중 하나를 랜덤하게 반환.
random.shuffle(a) - a 의 데이터 순서를 무작위로 섞어준다.
random.choice(a) - a 의 데이터중에서 랜덤하게 반환.
'''