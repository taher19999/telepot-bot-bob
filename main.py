import asyncio
import telepot
import telepot.aio
import pprint
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN = '5311863686:AAHLNjst3Wcbkrfouc4MnCVfxKz7Xnrp0V8'
bot = telepot.Bot(TOKEN)

async def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint.pprint(msg)
    if content_type == 'text':
        message=msg['text']
        await bot.sendMessage(chat_id,'Hi!')
        return

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

loop.run_forever()
