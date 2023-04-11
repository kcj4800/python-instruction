# Chapter09-2
# CSV 파일 읽기 및 쓰기
# CSV : MIME - text/csv #csv memetype
'''
# 파일 Write 실습
 - csv 파일 설명
 - csv.reader
 - csv.DictReader
 - csv.writer
 - csv 파일 전체 실습
'''


import csv

# 예제1
# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.reader(f) # reader = csv.reader(f, delimiter=',')가 정석이지만 csv의 c가 comma의 약자이므로 ,를 기본값으로 갖는다.
#     # next(reader) Header Skip
#     # 객체 확인
#     print(reader)
#     # 타입 확인
#     print(type(reader))
#     # 속성 확인
#     print(dir(reader))  # __iter__
#     print()
#     # print(list(reader))
#     print('~~~~'*30)
#     for c in reader:
#         # print(c)
#         # 타입 확인(리스트)
#         # print(type(c))
#         # list to str
#         # print(c)
#         print(' : '.join(c))
#     # print(list(reader))
#     print('~~~~'*30)

# # 예제2
# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')  # 구분자 선택
#     # next(reader) Header 스킵
#     # 확인

with open('./resource/test1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=',')
    print(type(reader))
    for i in reader:
        print(type(i))

#     for c in reader:
#         # print(c)
#         print(''.join(c)) # c의 리스트에 있는 내용을 붙여서 프린트해줌

a = [1,2,3,4,5]
b = ['돼지', '강아지', '고양이', '발발이', '치즈']
c=list(zip(a,b))
d=[]
f={}
# print(list(zip(a, b)))
for k, v in enumerate(b):
    f[k] = v
    d.append([str(k)+'번', v])
    print(f[k], d[k])
print(f,d)
print(type(d))
j=str()
# j = ''.join(d)
for i in d:
    h = ' : '.join(i)
    j = str(j) + '|' + str(h)
print(j,':::::') # str인 상태의 j
print(j.split('|'),'[][][]') # |를 기준으로 list로 나뉜 j
e = '돼지 꿀꿀이 마낭이'
g = e.split(' ')
print(g)

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],[13, 14, 15]]
with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    for v in w:
        csv.writer(f).writerow(v)

# for i in d:
#     print (''.join(i)) # 이런식으로 쓰는게 아닌가보다.

# # # 예제3 (Dict 변환)
# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     # 확인
#     print(reader)
#     print(type(reader))
#     print(dir(reader))  # __iter__ 확인
#     print()

#     for c in reader:
#         for k, v in c.items():
#             print(k, v)
#         print('-----')

# csv.reader(f, delimiter=',')를 사용해 불러오면 ,를 기준으로 나뉜 list형태로 불러온다.

# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',') # delimiter=','을 사용하면 ,를 기준으로 나눌 수 있다.
#     next(reader) # 헤더를 스킵한다.
#     a ={}
#     for i in reader:
#         a[i[0]]=i[1] # dict형태로 바꿀 수 있다.
#     print(a)

# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')
#     next(reader)
#     print(dict(reader)) # 좀더 단순하게 이렇게 dict타입으로 형변환 가능하다.


# with open('./resource/test1.csv', 'r') as f:
#     reader = csv.DictReader(f) # csv.DictReader(f) 로 가져오게되면 컬럼네임(필드네임 - 헤더)을 살릴 수 있다.
#     for c in reader:
#         for k, v in c.items():
#             print(k, v)
#         print('-----------')

# with open('./resource/test1.csv', 'r') as f: # csv.reader(f, delimiter=',')로 불러왔지만, 같은 결과를 낼 수 있다.
#     reader = csv.reader(f, delimiter=',')
#     a ={}
#     for i in reader:
#         a['Name']=i[0] 
#         a['Code']=i[1]
#         for k, v in a.items():
#             print(k, v)
#         print('------------')


# 예제4
# w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

# with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
#     print(dir(csv))
#     wt = csv.writer(f)
#     # dir 확인
#     print(dir(wt))
#     # 타입 확인
#     print(type(wt))
#     for v in w:
#         wt.writerow(v)
#         csv.writer(f).writerows('asdf')

# # 예제5
# with open('./resource/write2.csv', 'w', newline='') as f:
#     # 필드명
#     fields = ['one', 'two', 'three']
#     # Dict Writer 선언
#     wt = csv.DictWriter(f, fieldnames=fields)
#     # Herder Write
#     wt.writeheader()

#     for v in w:
#         wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})
with  open('./resource/write3.csv', 'w', newline='') as f:
    fileds=['one', 'two', 'three']
    wt = csv.DictWriter(f, fieldnames=fileds)
    wt.writeheader()
    for v in w:
        wt.writerow({fileds[0]:v[0],fileds[1]:v[1],fileds[2]:v[2]})


