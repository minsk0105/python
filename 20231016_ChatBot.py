import json # 필요한 데이터 조각을 추출할 수 있도록 json 모듈을 사용
import requests # 모듈 가져오기
import time # 요청 사이에 지연을 두기 위한 모듈 추가
import urllib
# 특수 문자를 인코딩(URL의 맥락에서 특별한 의미를 갖는 기호로 인해 발생)
import random # 숫자를 랜덤으로 출력

TOKEN = "6398049872:AAGwlITpxsj9uuS7y4AJbzGuA-xJo7P7ICA" # 텔레그램 api를 인증하는 데 필요한 봇의 토큰을 정의
URL = "https://api.telegram.org/bot{}/".format(TOKEN) # URL 생성

gamelist = {} # 딕셔너리 선언

def get_url(url): # URL에서 콘텐츠를 다운로드하고 문자열 제공
    response = requests.get(url) # 변수를 requests 형태로 저장
    content = response.content.decode("utf8") # 추가 호환성을 위해 utf8 부분추가
    return content # 저장된 변수를 반환

def get_json_from_url(url): # 문자열 응답을 가져옴
    content = get_url(url)
    js = json.loads(content) # python으로 사전 구문 분석
    return js # 저장된 변수를 반환

def get_updates(offset=None): # 함수에 선택적 매개변수 추가
    url = URL + "getUpdates?timeout=100" 
    # 업데이트가 있을 때까지 연결을 열어 둘 수 있도록 대기 시간을 지정 (timeout)
    # 이전에 브라우저에서 사용한 것과 동일한 API 명령을 호출
    if offset:
        url += "&offset={}".format(offset)
        # 추가 인수를 구분할 수 있도록 %offset={}로 지정
    js = get_json_from_url(url)
    return js # 해당 변수를 반환

def get_last_chat_id_and_text(updates):
    # 채팅 ID와 Bot에 전송된 가장 최근 메세지의 메세지 텍스트를 가져옴
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)
# Bot과 메세지를 보낸 사람 간의 채팅(chat_id)과 메세지(text)인 튜플을 반환

def send_message(text, chat_id):
    # 보내려는 메세지의 텍스트와 메세지를 보내려는 채팅의 채팅 ID를 가져옴
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    # API 명령을 호출, URL 매개변수로 전달하여 텔레그램에 메세지를 보내도록 요청
    get_url(url)

def get_last_update_id(updates):
    # getUpdates에서 수신하는 모든 업데이트 중 가장 높은 ID를 계산하는 함수 추가
    update_ids = []
    for update in updates["result"]:
        # 텔레그램에서 얻은 각 업데이트를 반복
        update_ids.append(int(update["update_id"]))
        # getUpdates를 다시 호출하여 ID를 전달
    return max(update_ids) # 반복한 후 가장 큰 ID를 반환

def echo_all(updates): # 수신한 각 메세지에 대해 응답을 보내는 함수 추가
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            # if(text == "/시간표"):
            #     send_message("원하시는 요일을 선택해 주세요.", chat)
            # elif(text in "mon"):
            #     send_message("월요일 : 프프프수성과영 / 시간 : 7교시", chat)
            # elif(text in "tue"):
            #     send_message("화요일 : 수국제제체사 / 시간 : 6교시", chat)
            # elif(text in "wed"):
            #     send_message("수요일 : 프프과수국사 / 시간 : 6교시", chat)
            # elif(text in "thu"):
            #     send_message("목요일 : 국과영진체음 / 시간 : 6교시", chat)
            # elif(text in "fri"):
            #     send_message("금요일 : 영사성음진로*3 / 시간 : 7교시", chat)
            # elif(text == "/stop"):
            #     send_message("서비스를 종료합니다. 알리미 봇을 이용해 주셔서 감사합니다.", chat)
            # elif(text == "/start"):
            #     send_message("안녕하세요. 인평자동차고등학교 시간표 알리미 봇 입니다. 시간표 일정을 원하시면 /시간표 를 입력해 주세요.", chat)
            if(text == "/numgame"): # 텍스트에 /numgame을 입력하면 실행
                rn = random.randrange(1, 101, 1)
                t_cnt=1
            # 1부터 100 사이의 숫자를 랜덤으로 지정하는 변수 추가
                send_message("1~100사이의 숫자를 입력하세요.", chat)
                # 텔레그램에 메세지를 전송
                print("game started with", chat, "/ Random Number:", rn)
                # 게임 시작과 동시에 숫자를 랜덤으로 지정
                gamelist[chat] = [rn, t_cnt, False]
            elif(text == "/stop"):
                send_message("Stop game.", chat)
                # /stop을 입력하면 게임을 종료
                gamelist[chat] = []
            elif(text == "/start"): # /start
                print("New user:", chat) # 터미널에 게임이 실행된 것을 표시
                send_message("게임을 시작하기 원하시면 /numgame 명령을 입력하세요. 게임을 멈추고 싶을 때는 /stop 명령을 입력하세요. ", chat)
            elif(len(gamelist[chat]) > 1 and not gamelist[chat][2]):
                num=int(text) # 텍스트에 숫자를 입력
                print(chat, "entered", text) # 채팅창에 텍스트를 입력했을 때 표시
                print("game status(entered) : ", gamelist) # 게임 상태 표시            
                if(num > gamelist[chat][0]): # 무작위로 지정한 숫자보다 입력한 숫자 값이 더 클 경우
                    send_message("Down", chat) # Down 메세지를 전송
                    gamelist[chat][1]+=1
                elif (num < gamelist[chat][0]): # 반대로 지정한 숫자보다 값이 작을 경우
                    send_message("Up", chat) # Up 메세지를 전송
                    gamelist[chat][1]+=1
                elif (num == gamelist[chat][0]): # 지정한 숫자와 입력한 숫자가 같을 경우
                    succeed = True # 정답
                    send_message("정답입니다.", chat) # "정답입니다."를 텔레그램에 전송한 이후
                    gamelist[chat][2] = succeed
                    if succeed:
                        text=str(gamelist[chat][1])+"번만에 정답을 맞히셨습니다."
                        # text에 입력한 횟수에 "번만에 정답을 맞히셨습니다."를 전송
                        send_message(text, chat)
                        send_message("게임을 종료합니다.", chat) # 메세지 전송
                        print(chat, "finished a game") # 게임 종료를 표시
                        gamelist[chat] = []
                        print("game status(finished) : ", gamelist)
        except Exception as e: # 예외 종류와 예외 객체에서 활용할 변수 이름
            print(e) # 예외가 발생했을 때 실행할 구문
   
def main():
    last_update_id = None # last_update_id = 비어있음
    while True: # while문 돌리기
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0: # 결과값의 길이가 0보다 클 때
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5) # 0.5초마다 가장 최근 메세지를 가져옴

if __name__ == '__main__': # __name__이라는 변수 값이 __main__일 때
# 아무것도 실행하지 않고 함수를 다른 스크립트로 가져옴
    main() # 메인 호출