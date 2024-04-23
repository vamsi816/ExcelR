import random
from rules import rules
import asyncio
from global_variable import api_token,group_chat_id
from telegram_bot import Telegram_Module
from telegram.error import TelegramError
from telegram.error import BadRequest


def is_co2_voilated(co2):
    co2_ll = round(float(rules['co2']['LL']),2)
    co2_ul = round(float(rules['co2']['UL']),2)
    if co2 < co2_ll or co2 > co2_ul:
        print(f'CO2 Alarm : CO2 is :{co2}, Lower Limit is {co2_ll}, Uper Limit is {co2_ul}')
        return True
    else:
        print(f'CO2 value read is :{co2}')
        return False

def is_temp_voilated(temp):
    temp_ll = round(float(rules['temp']['LL']),2)
    temp_ul = round(float(rules['temp']['UL']),2)
    if temp < temp_ll or temp > temp_ul:
        print(f'Temperature Alarm : Temp is :{temp}, Lower Limit is {temp_ll}, Uper Limit is {temp_ul}')
        return True
    else:
        print(f'Temperature value read is :{temp}')
        return False
    
def is_humidity_voilated(humidity):
    humidity_ll = round(float(rules['humidity']['LL']),2)
    humidity_ul = round(float(rules['humidity']['UL']),2)
    if humidity < humidity_ll or humidity > humidity_ul:
        print(f'Humidity Alarm : Humidity is :{humidity}, Lower Limit is {humidity_ll}, Uper Limit is {humidity_ul}')
        return True
    else:
        print(f'Humidity value read is :{humidity}')
        return False

def main():

    while True:
        break_yes = input('Please select 1 to stop: ')
        if break_yes == '1':
            break
        co2 = round(random.uniform(3600,4000),2)
        temp = round(random.uniform(10,40),2)
        humidity = round(random.uniform(50,80),2)

        print(f'CO2:{co2}PPM,Temp:{temp}Deg Celsius,Humidity:{humidity}%')
        
        violated_flg = is_co2_voilated(co2)
        print(violated_flg) 
        if violated_flg == True:
            print(f'CO2 levels violated. CO2 value is {co2}')
            asyncio.run(Telegram_Module.send_test_message(Telegram_Module(api_token, group_chat_id),"CO2 Violated"))
        else:
            pass
        
        violated_flg = is_temp_voilated(temp)
        print(violated_flg) 
        if violated_flg == True:
            print(f'Temperature levels violated. Temp value is {temp}')
            asyncio.run(Telegram_Module.send_test_message(Telegram_Module(api_token, group_chat_id),"Temp Violated"))
        else:
            pass
        
        violated_flg = is_humidity_voilated(humidity)
        print(violated_flg) 
        if violated_flg == True:
            print(f'Humidity levels violated. humidity value is {humidity}')
            asyncio.run(Telegram_Module.send_test_message(Telegram_Module(api_token, group_chat_id),"Humidity Violated"))
        else:
            pass
        
if __name__ == '__main__':
    main()