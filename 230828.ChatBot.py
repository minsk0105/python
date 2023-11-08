import json # 필요한 데이터 조각을 추출할 수 있도록 모듈을 사용하여 구문 분석
import requests # 모듈 가져오기
import time
import urllib

TOKEN = "6398049872:AAGwlITpxsj9uuS7y4AJbzGuA-xJo7P7ICA" # 에코봇을 실행할 텔레그램 토큰을 가져오기
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url): # get_url 함수 : URL에서 콘텐츠를 다운로드하고 문자열 제공
    response = requests.get(url)
    content = response.content.decode("utf8") # 추가 호환성을 위한 부분 추가
    return content


def get_json_from_url(url): 
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()