import re, random
from colorama import Fore, init

init(autoreset=True)

detination = {
    "beaches": ["Maldives", "Bora Bora", "Phuket", "Bahamas"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Paris", "Tokyo", "London"],
}

jokes = ["Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't programmers like nature? It has too many bugs!"]

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())

def recomend():
    print(Fore.CYAN + "Travel Bot: beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in detination:
        suggestion = random.choice(detination[preference])
        print(Fore.GREEN + f"Travel Bot: How about {suggestion}?")
        print(Fore.CYAN + "Travel Bot: Do you like it?(yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
     
        if answer == "yes":
            print(Fore.GREEN + "Travel Bot: Great! Have a wonderful trip!"
            "(Type 'exit' or 'bye' to end)")
        elif answer == "no":
            print(Fore.RED + "Travel Bot: Sorry to hear that. lets try again")
            recomend()
        else:
            print(Fore.RED + "Travel Bot: I'll suggest again.")
            recomend()
    else:
        print(Fore.RED + "Travel Bot: I didn't understand that. Let's try again.")
    
    show_help

def show_help():
    print(Fore.MAGENTA + "\n I can")
    print(Fore.GREEN + "Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "Tell you a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end\n")

def chat():
    print(Fore.CYAN + "I am Travel Bot.")
    name = input(Fore.YELLOW + "What's your name?")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recomend()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "Travel Bot: Goodbye!")
            break
        else:
            print(Fore.RED + "Travel Bot: Could you please rephrase that?")

if __name__ == "__main__":
    chat()