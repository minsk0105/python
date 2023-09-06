for i in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]: # 리스트 지정
    print("2 *", i ,"=", 2 * i)

for j in range(2, 10): # for문을 이용하여 단의 범위를 지정
    for i in range(1, 10): # j값에 몇을 곱할지를 지정
        print(j, "*", i, "=", j * i) # "{}x{}={}"형식의 출력폼
    print() #한 칸씩 띄움

x = 1 # 변수 지정
while x <=9: # 반복할 x값의 범위 지정

    y = 1 # 초기값
    if y % 2 !=0: #만약 y값이 홀수일 때
        while y <=9:
            print("{}*{}={}".format(x,y,x*y)) # 문제에 제시된 출력폼 사용
            y+=1 #증감식
        print()
    else:
        if y % 2==0: # y값이 짝수일 때
            while y <=9:
                input("{}*{} ={}".format(x,y,x*y)) # input 함수로 입력어 출력
                y+=1
        print()
    x+=1

print("2 * 1 = 2") # 직접 입력하여 출력
print("2 * 2 = 4")
print("2 * 3 = 6")
print("2 * 4 = 8")
print("2 * 5 = 10")
print("2 * 6 = 12")
print("2 * 7 = 14")
print("2 * 8 = 16")
print("2 * 9 = 18")

for i in range(2, 10, 3): # 2부터 9 사이에 값 중에서 3번 째 간격마다 값을 출력함
    print("2 *", i, "=", 2 * i)