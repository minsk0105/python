import pygame

pygame.init() # 초기화
screen_width = 1920 #화면의 가로 크기
screen_height = 1080 #화면의 세로 크기
screen = pygame.display.set_mode((screen_width, screen_width)) #실제 화면에 대한 정보를 불러오는 단계
pygame.display.set_caption("Game") #화면 상태바 이름 정의

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #프로그램 창을 닫으라는 명령 X 버튼을 눌렀는가를 확인
            running = False #더이상 while 문을 실행이 되지 않음.


pygame.quit() #게임을 종료하세요.