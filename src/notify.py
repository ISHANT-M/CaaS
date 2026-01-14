import requests
from environs import env


def send_telegram_msg(messages):
    env.read_env()
    # Get credentials from environment variables (Set these in GitHub Secrets/Local Env)
    token = env("TELEGRAM_TOKEN")
    chat_id = env("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Error: Missing Telegram credentials.")
        return
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "-------UPDATE-------"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("alive!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")


    for message in messages:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print("message sent!")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}")