print("Hello, I am your AI chatbot")
name = input("What is your name? ")
print("Nice to meet you, ",name,"!")
print("How is your mood today? (good/bad/neutral)")
mood = input().lower()
while mood in ["good", "bad", "neutral"]:
    if mood == "good":
        print("That's great to hear! Hope you have a nice day.")
    elif mood == "bad":
        print("I'm sorry to hear that. I hope things get better soon.")
    elif mood == "neutral":
        print("I see. Hope your day improves!")
    else:
        print("I see. Thanks for sharing your mood with me.")
    print("Would you like to chat more? (yes/no)")
    response = input().lower()
    if response == "yes":
        print("Great! What are your hobbies?")
        hobbies = input().lower()
        print("That's an interesting!")
        print("What are your favourite activities?")
        activities = input().lower()
        print("Sounds fun!")
    else:
        print("No problem! Have a great day, ",name,"!")
        break