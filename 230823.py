tuple_test = (10, 20, 30)

tuple_test[0]
print(tuple_test)

tuple_test[1]
print(tuple_test)

tuple_test[2]
print(tuple_test)

tuple_test[0] = 1
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test:)", type(tuple_test))
print()
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

a, b = b, a

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 함수를 선언함.
def test():
    return (10, 20)

# 여러 개의 값을 리턴받음.
a, b = test()

# 출력
print("a:", a)
print("b:", b)

# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

# 조합
call_10_times(print_hello)

numbers = [1,2,3,4,5,6]

print("::".join(map(str, numbers)))

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3<=x<7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x * x < 50, numbers)))