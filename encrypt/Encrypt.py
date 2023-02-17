#문자 암호화하기

#사용할 아스키 범위
asciiMin = 32    #공백
asciiMax = 126   #물결

#암호화 키
key = 314159
key = str(key)

#암호화할 메세지 입력받기
message = input("암호화할 메세지를 입력하세요: ")

#암호화 메세지용 변수 초기화하기
messEncr = ""

#메세지 루프
for index in range(0, len(message)) :
    char = ord(message[index])

    if char < asciiMin or char > asciiMax :
        messEncr += message[index]
    else :
        ascNum = char + int(key[index % len(key)])

        if ascNum > asciiMax:
            ascNum -= (asciiMax - asciiMin)
        
        messEncr = messEncr + chr(ascNum)


print("암호화 된 메세지 : "+messEncr)
