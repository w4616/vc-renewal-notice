import requests
import json
import logging
import datetime

today = datetime.date.today()
aftertomorrow = today + datetime.timedelta(days=2)
idurl = f'http://你的api域名或者ip/du.php?date={aftertomorrow}'
req = requests.get(url=idurl)
if req.text == "No results found.":
    print('没有需要推送的任务')
else:

    data = json.loads(req.text)
    ids = [d['id'] for d in data]
    logging.basicConfig(filename=f'log2_{today}.txt', level=logging.INFO)

    # Step 2: Send a message to each user
    api_key = '你的tg token'
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    text = f'您的VPS将在{aftertomorrow}到期\n如果您已续期可使用 /renew 自动计算保存时间\n测试阶段，bug反馈 @qjpm_bot'

    for chat_id in ids:
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(url, data=params)
        try:
            logging.info(f'Sent message to {chat_id}. Response: {response.json()}')
        except Exception as e:
            logging.info(f'错误{chat_id}，{response.status_code}')