from calmbot import CalmBot

def main():
    bot = CalmBot(verbose=True)
    user_input = input("Please paste your error here, and traceback if you have any:\n ")
    response = bot.handle_error_text(user_input)
    print(response)

if __name__ == "__main__":
    main()
