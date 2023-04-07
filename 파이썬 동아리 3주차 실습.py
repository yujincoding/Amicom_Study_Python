# a = input("값: ")
# print(a)
# c = a.split(" ")
# print(c)

# 과제 1
words = ["bird", "rat", "eagle", "cat"]
print(words)
oldword = input("바꿀 단어를 입력하시오.: ")
newword = input("새로운 단어를 입력하시오.: ")

words.insert(words.index(oldword), newword)
words.pop(words.index(oldword) + 1)

print(words)

# 과제 2
user = {}
userData = input("사용자 정보를 입력해주세요.(이름, 나이, 학년): ")

userSplit = userData.split(" ")
# print(userSplit, type(userSplit))

user[userSplit[0]] = userSplit[1], userSplit[2]
# print(user, type(user))

name = input("조회하고자 하는 사용자 이름을 입력해주세요.: ")
address = list(user[userSplit[0]])
# print(address)
print("이름: {} 나이: {} 학년: {}".format(userSplit[0], address[0], address[1]))