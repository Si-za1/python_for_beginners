# using VADER for the mood catcher 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from openai import OpenAI
#assuming this to be the journal entry in the JSON format 
journal_entry = [
  {
    "date": "2025-06-01",
    "entry": "Today was amazing! I finished my project early and went for a walk. The sunset was beautiful."
  },
  {
    "date": "2025-06-02",
    "entry": "I felt really anxious during my meeting. Nothing seemed to go right, and I was stressed out."
  },
  {
    "date": "2025-06-03",
    "entry": "Just a normal day. Worked a bit, cleaned the apartment, and watched some TV."
  },
  {
    "date": "2025-06-04",
    "entry": "I'm feeling really low. Everything feels heavy and I don't know what to do."
  },
  {
    "date": "2025-06-06",
    "entry": "Had lunch with an old friend! We laughed a lot and caught up on everything."
  }
]

#now the above json format will be used for the sentence analysis
analyzer = SentimentIntensityAnalyzer()

for entry in journal_entry:

    text = entry['entry']
    polarity_analyze = analyzer.polarity_scores(text)

    compound = polarity_analyze["compound"]

    if compound >= 0.5:
        mood = "Positive"
    elif compound <= -0.5:
        mood = "Negative"
    else:
        mood = "Neutral"

    #for each journal entry 
    entry["mood"] = mood
    entry["compound_score"] = compound

#now if i want to know how was my mood on this date based on my entry

def get_entry_date(date):
    for entry in journal_entry:
        if entry["date"] == date:
            return entry
        return None

def get_my_mood(date):
    date_entry = get_entry_date(date)

    if date_entry is not None:
        client = OpenAI(api_key="your-key")

        prompt = f"""
        based on the entered {date_entry} and tell me what was my day like, 
        , and explain why in 100 words:
        Journal Entry: "{entry['entry']}"
        Mood Score: {entry['compound_score']} ({entry['mood']})
        Give me one word for my mood on that day, as the indicator.
        """

        response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens= 100,
        temperature= 0.6,
        messages=[
            {"role": "system", "content":prompt}
        ]
        )

        # print(response.choices[0].message.content)
    return response.choices[0].message.content
    # return response['choices'][0]['message']['content']

if __name__ == "__main__":
    date = "2025-06-01"
    # print(f"I want to know my mood on {date}")
    print(get_my_mood(date))

