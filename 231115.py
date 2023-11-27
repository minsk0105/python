import random
import sys
import os
# print(sys.argv)
# print("# rnadom 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
# print("- random():", random.random())

# uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
# print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 값을 리턴
# -randrange(min, max): min부터 max 사이의 값을 리턴
# print("- randrange(10)", random.randrange(10, 20))

# print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))


# print("---")

# print("getwindowsversion:()", sys.getwindowsversion())
# print("---")
# print("copyright:", sys.copyright)
# print("---")
# print("version:", sys.version)

# sys.exit()

print("현재 운영체제:", os.name)
print("헌재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())


os.mkdir("hello")
os.rmdir("hello")