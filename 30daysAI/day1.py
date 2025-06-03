# affirmation generator

from openai import OpenAI

def user_choice_genre():
    genres = ["motivational", "inspirational", "emotional"]
    user_choice = input(f"the quote genre that you want to choose from {genres}: ")
    if user_choice not in genres:
        print("the genre that you have chosen is invalid")
        user_choice = input(f"Choose a quote genre from {genres}: ")
    return user_choice


# initializing the openai api
def affirm_generation(user_choice):
    client = OpenAI(
        api_key="YOUR OPEN AI API KEY ")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"you are a motivational and inspirational quote generator. You will generate a quote based on the genre that the user has chosen. The genre that the user has chosen is {user_choice}. The quote should be {user_choice} and should be less than 50 words."},
            {"role": "user", "content": "generate a quote based on the genre that the user has chosen"}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


if __name__ == "__main__":
    user_choice = user_choice_genre()
    affirm_generation(user_choice)
