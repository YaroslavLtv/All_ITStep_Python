import requests
import random
my_secret_name = "1492394985:AAFiDW0F6Mi6C3VUXL8_XCXfdWIwqWRDbM8"
url = f"https://api.telegram.org/bot{my_secret_name}/"


def last_update(request):
    response = requests.get(request + "getUpdates")
    response = response.json()
    results = response["result"]
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id


def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


def send_message(chat, text):
    params = {"chat_id": chat, "text": text}
    response = requests.post(url + "sendMessage", data=params)
    return response


def main():
    faq = {"who": "ITStep Cloud", "where": "Earth"}
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi":
                send_message(get_chat_id(update), "Hello, i am Robot!")
            # Тут можуть бути власні команди
            elif get_message_text(update).lower() == "dice":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update), f"{_1} and {_2}")
            elif get_message_text(update).lower() in faq:
                send_message(get_chat_id(update), f"{faq[get_message_text(update).lower()]}")
            else:
                send_message(get_chat_id(update), "Sorry, i don't understand you")
            update_id = update_id + 1


if __name__ == "__main__":
    main()
