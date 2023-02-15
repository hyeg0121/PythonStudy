import random

print("주사위 굴리기...")
die1 = random.randrange(1, 7)
die2 = random.randrange(1, 7)
print("나온 수는 ", die1, ",", die2, "입니다.")

# TODO : 두명의 플레이어가 굴려서 점수 비교, 더블일 때 한번 더