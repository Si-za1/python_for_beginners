import random
import time
import threading
import openai
from openai import OpenAI

# openai.api_key = ""

user_choice = "emotionally intelligent"


def alert_time(min_minutes=1, max_minutes=1):
    return random.randint(min_minutes * 60, max_minutes * 60)


def reminder_generation():
    client = OpenAI(api_key="--")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.6,
        messages=[
            {"role": "system", "content": f"You are a motivational and inspirational quote generator. Generate a quote that is {user_choice}, under 50 words."},
            {"role": "user", "content": "Give me a quote based on the chosen theme."}
        ]
    )
    quote = response.choices[0].message.content
    print(f"\n💬 Reminder: {quote}")


def loop_time():
    while True:
        delay = alert_time(1, 1)
        print(f"⏳ Waiting {delay // 60} minute(s)...")
        time.sleep(delay)
        reminder_generation()


if __name__ == "__main__":
    print("✨ Self-Care Reminder App Started!")
    reminder_thread = threading.Thread(target=loop_time)
    reminder_thread.daemon = True
    reminder_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Take care.")
