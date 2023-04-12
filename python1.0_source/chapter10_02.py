# Chapter10-2
# Hangman(행맨) 미니게임 제작(2)
# 프로그램 완성 및 최종 테스트
'''
# Hangman 미니 게임 제작(2)
 - Winsound 설명
 - 무작위 단어 선택 추가
 - 단어 힌트 추가
 - 사운드 추가하기
 - 최종 프로그램 테스트
 - 앞으로 공부하면 좋은 파트 추천
'''

# 시간 처리
import time
# 랜덤
import random
# csv 처리
import csv
# 사운드 처리
import winsound
#처음 인사
# name = input("What is your name? ")

# print("Hi!, " + name, "Time to play hangman game!")

# print()

# #1초 대기
# time.sleep(1)

# print("Start loading...")
# print()

# # 0.5초 대기
# time.sleep(0.5)

# # CSV 단어 리스트
# words = []

# # 문제 CSV 파일 로드
# with open('./resource/word_list.csv', 'r') as f:
# 	reader = csv.reader(f)
# 	# Header Skip
# 	next(reader)
# 	for c in reader:
# 		words.append(c)

# # 리스트 섞기
# random.shuffle(words)
# # 임의의 단어 선택
# q = random.choice(words)

# #정답 단어
# word = q[0].strip()

# #추측 단어
# guesses = ''

# #기회
# turns = 10

# # 핵심 While Loop
# # 찬스 카운트가 남아 있을 경우
# while turns > 0:
#     # 실패 횟수
#     failed = 0

#     # 정답 단어 반복
#     for char in word:
#         # 정답 단어 내에 추측 단어가 포함되어 있는 경우
#         if char in guesses:
#             # 추측 단어 출력
#             print (char, end=' ')
#         else:
#             # 틀린 경우 대시로 처리
#             print ("_", end=' ')
#             # 실패 횟수 증가
#             failed += 1

#     # 단어 추측이 성공한 경우
#     if failed == 0:
#         print()
#         print()
# 		# 성공 사운드
#         winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
# 		# 축하 메시지
#         print("Congratulations! The Guesses is correct.")
#         # while 구문 중단
#         break

#     print()
#     # 추측 단어 글자 단위 입력
#     print()
#     print('Hint : {}'.format(q[1].strip()))
#     guess = input("guess a character:")

#     # 단어 더하기
#     guesses += guess

#     # 정답 단어에 추측한 문자가 포함되어 있지 않으면
#     if guess not in word:
#         # 기회 횟수 감소
#         turns -= 1
#         # 오류 메시지
#         print("Oops! Wrong")
#         # 남은 기회 출력
#         print("You have", + turns, 'more guesses!')

#         # 기회를 모두 사용하면
#         if turns == 0:
# 			# 탈락 사운드
#             winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
#             # 실패 메시지
#             print("You hangman game failed. Bye!")

name = input('Please Enter your name :')
print('Hello', name, 'Welcome to Hang-man game world!')
time.sleep(0.5)
print('Now loading..')
time.sleep(0.5)
print('Start!')
chances = 10
Monster = ['goblin', 'gargoyle', 'gryphon', 'harpy', 'orc', 'ogre', 'troll', 'wyvern', 'dragon']
fruit = ['watermelon', 'lime', 'grapefruit', 'pineapple', 'mango', 'strawberry', 'melon', 'orange', 'grape']
vehicle = ['wagon', 'sedan', 'van', 'bike', 'bicycle']
words=[]

with open('./resource/word_list.csv', 'w') as f:
    fields = ['Name', 'Hint']
    writer = csv.DictWriter(f, fieldnames=fields)
    for v in Monster:
        writer.writerow({fields[0]: v, fields[1]:'monster'})
    for v in fruit:
        writer.writerow({fields[0]: v, fields[1]:'fruit'})
    for v in vehicle:
        writer.writerow({fields[0]: v, fields[1]:'vehicle'})
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for v in reader:
        words.append(v)

words = [v for v in words if v] # 리스트 안의 null값을 제거해 주는 방법 1
'''
# 다양한 방법으로 리스트 안에 null값을 제거해줄 수 있다.
# words = list(filter(None, words))
# words = list(filter(bool, words))
# words = list(filter(len, words))
# words = list(filter(lambda v: v, words))
'''
word = random.choice(words)
guesses = ''
for i in word[0]:
    print('_', end=' ')
print()
while chances > 0:
    print('Hint :', word[1])
    print('you have', chances,'more chances')
    guess = input('guess a charater :')
    guesses += guess
    chances -= 1
    failed  = 0
    for char in word[0]:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    print()


    if failed == 0:
        print('congraturation!!')
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        break
    elif chances == 0:
        print('You failed!')
        print('The answer is ', word[0])
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        break








