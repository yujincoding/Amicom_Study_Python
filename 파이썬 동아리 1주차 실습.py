# 과제 1

from random import *

number = int(random() * 29) +1
print(number + "개")

# 과제 2

print("  A\n BC\nDEF")

# 과제 3

from random import *

age = int(randrange(10, 31))
name = input("이름을 영어로 입력하시오.: ")
name = name.lower()

print("안녕하세요. 제 이름은", name.title(), "이고, 제 나이는", age, "입니다.")