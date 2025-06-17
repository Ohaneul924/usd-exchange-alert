import requests
import schedule
import time

TOKEN = '7627124447:AAENNOL8sZv8Gs85MTReLDCMxxoIKwLEk7M'
CHAT_ID = '7697525666'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

def get_exchange_rate():
    url = "https://api.frankfurter.app/latest?from=USD&to=KRW,EUR,JPY"
    response = requests.get(url)
    data = response.json()

    print("API 응답:", data)

    krw = data['rates']['KRW']
    eur = data['rates']['EUR']
    jpy = data['rates']['JPY']

    message = f"📢 환율 정보 (USD 기준)\n🇰🇷 KRW: {krw:.2f}\n🇪🇺 EUR: {eur:.2f}\n🇯🇵 JPY: {jpy:.2f}"
    print(message)
    send_telegram_message(message)

# 최초 실행
get_exchange_rate()
schedule.every(1).hours.do(get_exchange_rate)

while True:
    schedule.run_pending()
    time.sleep(1)
