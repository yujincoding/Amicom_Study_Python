# 과제 1
today = int(input("오늘 일자를 입력해주세요.(1~31): "))
if today % 4 == 0:
    print("오늘은 장날입니다.")
else:
    print("오늘은 장날이 아닙니다.")

# 과제 2
user = {}

for inform in range (3):
    userData = input("사용자 정보를 입력해주세요.(이름, 나이, 학년): ")
    userSplit = userData.split(" ")
    user[userSplit[0]] = [userSplit[1], userSplit[2]]
print(user)

# 과제 3
def calculator():
    print("계산기를 작동합니다.\n\n")
    calculate = int(input("원하는 연산 번호를 입력해주세요. (1. 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈): "))
    one_num = int(input("첫 번째 수를 입력해주세요.: "))
    two_num = int(input("두 번째 수를 입력해주세요.: "))
    if calculate == 1:
        print("결과값: {}".format(one_num + two_num))
    elif calculate == 2:
        print("결과값: {}".format(one_num - two_num))
    elif calculate == 3:
        print("결과값: {}".format(one_num * two_num))
    else:
        print("결과값: {}".format(one_num / two_num))
calculator()

# 과제 4

for i in range (1, 6):
    print(" "*(5-i), end = " ")
    print("*"*(2*i-1))

n = 5
for i in range(n):
    print(" " * (n - (i + 1)), end = " ")
    print("+" * (2 * i + 1))