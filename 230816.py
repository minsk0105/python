# 팩토리얼 함수로 구현하기
# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output *= i
#     return output

# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))
# print("25!:", factorial(25))
# print("1300!:", factorial(1300))

# 팩토리얼 재귀함수로 구현하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 55ad0e8 (.)
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
<<<<<<< HEAD
=======
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
>>>>>>> 1c4ac3b (.)
=======
>>>>>>> 55ad0e8 (.)
print("5!:", factorial(5))