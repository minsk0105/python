# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5)

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")
# print_n_times("안녕하세요", 10, 20)

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# n = int(input("몇번 반복할지 입력하세요 : "))

# print_n_times(n, "안","녕","하")

def mul(*values):
    out = 1
    for value in values:
        out = out * value
    return out

print(mul(5, 7, 9, 10))