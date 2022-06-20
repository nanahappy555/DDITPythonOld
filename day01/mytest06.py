# 홀짝을 입력하시오
# 나 홀
# 컴 홀
# 결과 이김

# 나 홀
# 컴 짝
# 결과 짐

# 컴퓨터가 뽑은 걸 맞추면 이김

import random 

me = input("홀/짝을 입력하시오 : ")
num = random.randint(1,2)


com = ""
if num == 1 :
    com = "홀"
else :
    com = "짝"

print("나 : "+me)
print("컴 : "+com)

if (com == me):
    print("결과 : 이김")
else :
    print("결과 : 짐")
