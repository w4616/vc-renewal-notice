import requests
import json
import logging
import datetime
import time

today = datetime.date.today()
#tomorrow = today + datetime.timedelta(days=1)
idurl = f'http://你的api域名或者ip/du.php?date=0000-00-00'
req = requests.get(url=idurl)
if req.text == "No results found.":
    print('没有需要推送的任务')
else:

    data = json.loads(req.text)
    ids = [d['id'] for d in data]
    logging.basicConfig(filename=f'q0log_{today}.txt', level=logging.INFO)

    # Step 2: Send a message to each user
    api_key = '你的tg token'
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    text = f'您输入的到期时间输入有误，已经删除！请重新输入！！!'

    for chat_id in ids:
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(url, data=params)
        time.sleep(1)
        try:
            logging.info(f'Sent message to {chat_id}. Response: {response.json()}')
        except Exception as e:
            logging.info(f'错误{chat_id}，{response.status_code}')
url000 = 'http://你的api域名或者ip/remove.php?date=0000-00-00'
q000 = requests.get(url=url000)
print(q000.text)