#숫자 맞히기 게임 만들기
import random

userInput = ""
userGuess = 0

randNum = random.randrange(1, 101)

print("1과 100사이 숫자 하나를 정했습니다.")
print("이 숫자는 무엇일까요?")

while randNum != userGuess:
    userInput = input("입력: ").strip()

    if not userInput.isnumeric():
        print("숫자를 입력하세요.")
    else:
        userGuess = int(userInput)

        if userGuess < randNum:
            print("더 큰 숫자를 입력하세요")
        elif userGuess > randNum:
            print("더 작은 숫자를 입력하세요.")
        else:
            print("정답입니다!")
