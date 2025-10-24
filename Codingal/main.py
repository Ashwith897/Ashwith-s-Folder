print("Hello, I am your AI chatbot")
name = input("What is your name? ")
print("Nice to meet you, ",name,"!")
print("How is your mood today? (good/bad/mid)")
mood = input()
while mood in ["good", "bad", "mid"]:
    if mood == "good":
        print("That's great to hear! Hope you have a nice day.")
    elif mood == "bad":
        print("I'm sorry to hear that. I hope things get better soon.")
    elif mood == "mid":
        print("I see. Hope your day improves!")
    else:
        print("I see. Thanks for sharing your mood with me.")
    print("Would you like to chat more? (yes/no)")
    response = input()
    if response == "yes":
        print("Great! What are your hobbies?")
        hobbies = input()
        print("That's an interesting!")
        print("What are your favourite activities?")
        activities = input()
        print("Sounds fun!")
        break
    else:
        print("No problem! Have a great day, ",name,"!")
        continue