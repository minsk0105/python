nums = list(range(2,7,2))
print(nums)

list_a = ["가", "나", "다", "라", "마"]
for out_list_a in list_a[4]:
  print(out_list_a)

list_a = [0,1,2,3]
list_a.append(5)
print(list_a)

list_a = [10,20,30,40,50]
list_a.clear()
print(list_a)

list_a = [2]
list_b = [1]
for list_a_o in list_a:
  for list_b_o in list_b:
    print(list_a_o)

import math
pi = 3.14152
print(round(pi,3))

name_dic = {"name1":"남궁민", "name2":"안은진"}
for key in name_dic:
  print(name_dic["name2"])

list_a = [0,1,2,3,4,5,6,7,8,9]
sum = 0
for i in range(len(list_a)):
  sum = sum+i
print(sum)

def fn(a, b, c, d, e):
  print(a, b, c, d, e)

fn (12,12,34,56,44)

def hello(msg="안녕하세요"):
  print(msg + "!")
hello()

def fn(a, b=[]):
  b.append(a)
  print(b)
fn(4)

def sum(*numbers):
  sum_value = 0
  for number in numbers:
    sum_value = sum_value + number
  return sum_value

result = sum(1,3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1,3,5,7))

with open("basic.txt","w") as file:
  file.write("good luck")
with open("basic.txt", "r") as file:
  contents = file.read()
print(contents)

arr = [1, 2, 3]
try:
  print(arr[5])
except:
 print("리스트의 요소에 접근하지 못했습니다.")

 # 2학기 기말고사 프로그램 시험 소스코드