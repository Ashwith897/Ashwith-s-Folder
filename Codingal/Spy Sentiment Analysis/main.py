import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for color output
colorama.init(autoreset=False)

print(f"{Fore.CYAN}Welcome to sentiment spy{Style.RESET_ALL}")

# Ask for username
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "sam"

# Storing conversation as a list of tuples
conversation_history = []

print(f"\n{Fore.CYAN}Hello agent {user_name}{Style.RESET_ALL}")
print(f"{Fore.CYAN}Type the sentence and I will analyze the sentiment.{Style.RESET_ALL}")
print(f"Type {Fore.YELLOW}'Reset'{Style.RESET_ALL}, {Fore.YELLOW}'History'{Style.RESET_ALL}, or {Fore.YELLOW}'Exit'{Style.RESET_ALL} to quit.\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid input.{Style.RESET_ALL}")
        continue

    cmd = user_input.lower()

    if cmd == "exit":
        print(f"{Fore.GREEN}Goodbye agent {user_name}!{Style.RESET_ALL}")
        break

    if cmd == "reset":
        conversation_history.clear()
        print(f'{Fore.CYAN}Conversation history cleared.{Style.RESET_ALL}')
        continue

    if cmd == "history":
        if not conversation_history:
            print(f"{Fore.CYAN}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # --- If we reach here, it's not a command: analyze sentiment ---
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} Sentiment Detected (Polarity: {polarity:.2f}){Style.RESET_ALL}")