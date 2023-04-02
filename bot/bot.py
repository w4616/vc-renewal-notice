import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
import sys

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="测试中，可能会不稳定输入 /help 获取帮助")

def time(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="命令已修改，请重新 /help 获取帮助")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/date 2023-4-1 (到期时间)手动输入到期时间\n/ck xxxxxx (cookie)自动获取到期时间\n/del 删除保存的时间\n/ping 检查存活\n/find 查询\n/renew 续期(以今天自动计算时间)")

def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="pong")

def renew(update, context):
    userid = update.effective_chat.id
    import datetime
    today = datetime.date.today()
    xday = today + datetime.timedelta(days=9)
    addurl = f'http://你的api域名或者ip/revise.php?id={userid}&date={xday}'
    addlog = requests.get(url=addurl)
    text = f'{addlog.text}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def add1(update, context):
    userid = update.effective_chat.id
    userdate = update.message.text[6:]
    inquire = f'http://你的api域名或者ip/id.php?id={userid}'
    inquirelog = requests.get(url=inquire)
    if inquirelog.text == 'yes':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'id{userid}已经存在数据库中')
    else:
        if userdate == '':
            context.bot.send_message(chat_id=update.effective_chat.id, text='时间错误!')
        else:
            addurl = f'http://你的api域名或者ip/xie.php?id={userid}&date={userdate}'
            addlog = requests.get(url=addurl)
            text = f'{addlog.text}'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def deleteid(update, context):
    userid = update.effective_chat.id
    dllurl = f'http://你的api域名或者ip/removeid.php?id={userid}'
    dlllog = requests.get(url=dllurl)
    context.bot.send_message(chat_id=update.effective_chat.id, text=dlllog.text)

def ckdate(update, context):
    userid = update.effective_chat.id
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://free.vps.vc/vps-info',
    'Alt-Used': 'free.vps.vc',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
    
    userck = update.message.text[4:]
    cookies = {
    'PHPSESSID': userck,
}
    response = requests.get('https://free.vps.vc/vps-info', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        rows = soup.find_all("div", class_="row mb-4")
        second_row = rows[1]
        text = second_row.get_text()
        text = text.replace('Valid until', '').strip()
        from datetime import datetime
        date_obj = datetime.strptime(text, '%B %d, %Y')
        userdate = date_obj.strftime('%Y-%m-%d')
        a = 1
    except Exception as e:
        a = 0
    inquire = f'http://你的api域名或者ip/id.php?id={userid}'
    findid = f'http://你的api域名或者ip/findid.php?id={userid}'
    inquirelog = requests.get(url=inquire)
    if a == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text='获取到期时间错误！')
    else:
        if inquirelog.text == 'yes':
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'id{userid}已经存在数据库中')
        else:
            if userdate == '':
                context.bot.send_message(chat_id=update.effective_chat.id, text='时间错误!')
            else:
                addurl = f'http://你的api域名或者ip/xie.php?id={userid}&date={userdate}'
                addlog = requests.get(url=addurl)
                finfid = requests.get(url=findid)
                text = f'{addlog.text}\n查询结果:{finfid.text}\n请以查询结果为准'
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def find(update, context):
    userid = update.effective_chat.id
    findid = f'http://你的api域名或者ip/findid.php?id={userid}'
    finfid = requests.get(url=findid)
    context.bot.send_message(chat_id=update.effective_chat.id, text=finfid.text)

def main():
    updater = Updater(token='你的tg token', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('date', add1))
    dispatcher.add_handler(CommandHandler('del', deleteid))
    dispatcher.add_handler(CommandHandler('ck', ckdate))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('ping', ping))
    dispatcher.add_handler(CommandHandler('find', find))
    dispatcher.add_handler(CommandHandler('renew', renew))
    dispatcher.add_handler(CommandHandler('time', time))
    updater.start_polling()

if __name__ == '__main__':
    main()
