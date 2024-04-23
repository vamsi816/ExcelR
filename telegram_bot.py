from telegram import Bot
from global_variable import api_token,group_chat_id


class Telegram_Module():
    
    def __init__(self,api_token,group_chat_id) :
        self.bot_token = api_token
        self.group_chat_id = group_chat_id

    async def send_test_message(self, message):
        #Create an instance of the Telegram Bot class
        bot = Bot(token=self.bot_token)#you need to the pass the BOT token ID
        await bot.send_message(chat_id=self.group_chat_id, text=message)
