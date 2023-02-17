#리스트 만들기
animals = list()
animals = ["개", "고양이", "사자", "호랑이", "병아리", "쿼카"]

#요소의 개수
print(len(animals))

#요소 바꾸기
animals[2] = "송아지"

#리스트 출력하기
print(animals)

#요소 추가하기
animals.append("여우")
print(len(animals))
print(animals)

#루프1
for animal in animals:
    print(animal)

print("--------")
#루프2
for i in range(0, len(animals)):
    print(animals[i])

    