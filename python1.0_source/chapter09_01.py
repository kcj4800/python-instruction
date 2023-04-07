# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1
# 변수 f를 통해 open 함수로 파일을 불러오고 f.close()를 통해 열려있는 변수 f를 닫아준다.
f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # UTF-8이 기본값으로 설정된다.
# f = open('.\\resource\\it_news.txt', 'rt', encoding='UTF-8') # 상대경로2 rt가 정석이지만 t는 기본값이므로 r이라고 해도 된다.
# f = open('C:/users/chan/python study/python1.0_source/resource/it_news.txt', 'r', encoding='UTF-8') # 절대경로
# f = open('C:\\users\\chan\\python study\\python1.0_source\\resource\\it_news.txt', 'r', encoding='UTF-8') # 절대경로2

# 속성 확인
print(dir(f))
# print(dir(f))
# print(f.encoding)
# print(f.name)
# cts = f.read()
# print(cts)
# f.close()
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read() # cts라는 컨텐츠 변수에 f.read()를 담아본다.
print(cts)
# 반드시 close
f.close()

# print()
# print('+++'*30)
# g = open('C:/users/chan/python study/python1.0_source/resource/it_news.txt', 'r', encoding='UTF-8')
# print(g.read())
# print(g.name)
# print(g.encoding)
# print(g.mode)
# print()
# print(g.__dir__) # 클래스에서 쓰는 건가..? <built-in method __dir__of_io.TextIOWrapper object at 0x000001D384762810>
# print()
# print(dir(g))
# g.close()
# print('+++'*30)
# print()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# with open('./resource/it_news.txt','r', encoding='UTF-8') as f:
#     c = f.read()
#     print(c)
#     print(iter(c))
#     print(list(c))




# 예제3
# read() : 전체 읽기 , read(10) : 10Byte

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as g:
    print(g.read(10))
    print(g.readline())
    print()
    print(g.read(10))
    print()
    print(g.seek(0, 0)) # from 0 to 0의 위치로 커서를 옮긴다.
    print(g.seek(0, 1))
    print(g.read(30))
    print(g.seek(0, 2))
    print(g.seek(0, 0))
    print()
    print(g.read(30))
    print(g.read(30),"++++++++++", len(g.read(30)), "++++++", g.read(30))
    print('+++'*30)



# 예제4
# readline : 한 줄 씩 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
        
print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')
    
    
# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
    
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as r:
    ww = (r.read())
    r.seek(0,0)
    www = (r.readlines())
    r.seek(0,0)
    with open('./resource/manang.txt', 'w', encoding='UTF-8') as f:
        f.writelines(r.readlines()) # 이런식으로 직접 읽어와서 파일에 쓰기 위해서는 seek(0, 0)을 활용해서 커서를 초기화 해줘야한다.
        r.seek(0,0)
        print(r.readlines())
        r.seek(0,0)
        f.write(r.read())
        r.seek(0,0)
    with open('./resource/manang.txt', 'a', encoding='UTF-8') as f:
        f.write(ww) # 위와 같은 내용을 담지만 불러온 내용을 변수에 선언하여 담아야 seek(0, 0)으로 초기화 해줄 필요가 없어 사용하기 편리하다.
        f.writelines(www)
print('==='*30)
print(ww)
print(www)
print('==='*30)
# print(r.read()) # with 문을 벗어나서는 호출할 수 없다.
print(ww) # with문 내에서 선언된 변수는 with문 밖에서도 사용 가능!

# 인코딩을 제대로 지정해 주지 않으면, 파일을 불러올때 글자가 깨질 수도 있다.
with open('./resource/mannnnang.txt', 'w') as f:
    f.write('Manang이')
with open('./resource/mannnnang.txt', 'a') as f:
    f.write(ww)
    f.writelines(www)


# 예제4 # print문의 여러 옵션(sep='', end='', flush, file) 중 file옵션을 사용하여 입력해 줄 수 있다.
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    f.write('Test Text Write!') 

# 이렇게 쓸수 있기 때문에 자주 쓰이지는 않지만 print문이 많이 있지만 콘솔에는 출력 되지 않을때 파일 옵션이 있는지 확인해 볼 필요가 있다.