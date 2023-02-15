#라이브러리 불러오기
import random

num = random.randrange(1, 11)
print("무작위 숫자 : ", num)

str = "앞뒤"
print(random.choice(str), "입니다")

str_list = ["앞면", "뒷면"]
print(random.choices(str_list))