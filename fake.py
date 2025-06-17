import random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

names = [
    "Ramesh Tripathi", "Priya Sharma", "John D’Souza", "Aarti Mehta",
    "Babloo Yadav", "Sneha Rajput", "Akash Verma", "Neha Kaur",
    "Raj Malhotra", "Tanya Singh"
]

actions = [
    "stole 500 coconuts", "declared himself the king of the colony",
    "opened a tea stall on the moon", "got stuck in a washing machine for 2 hours",
    "started a new religion based on potatoes", "tried to marry a robot",
    "danced on the roof for 10 hours", "painted all street dogs pink",
    "fought with a mirror thinking it was a ghost", "banned Monday in his village"
]

places = [
    "Kanpur Zoo", "Sector 13, Noida", "Moon Market, Lahore",
    "Under the flyover near Andheri", "A haunted dhaba in Rajasthan",
    "Cyber Café, Lajpat Nagar", "Middle of Yamuna River",
    "A local marriage hall in Bihar", "On top of Qutub Minar",
    "Dadar Railway Station's waiting room"
]

emojis = ["😂", "😱", "🫣", "🚨", "🤯", "🙈"]

while True:
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)
    reaction = random.choice(emojis)
    timestamp = datetime.now().strftime("%d %B %Y, %I:%M %p")

    ans = f"BREAKING NEWS: {name} {action} at {place} {reaction}!"
    print("\n" + Fore.RED + Style.BRIGHT + ans)
    print(Fore.YELLOW + "🕒 " + timestamp)

    # Save to file
    with open("fake_news_archive.txt", "a", encoding="utf-8") as file:
        file.write(f"{ans} - {timestamp}\n")

    user_input = input(Fore.WHITE + "\nDo you want another news? (yes/no): ").lower()
    if user_input == "no":
        break

print(Fore.GREEN + "\nThank you for using fake news generator. Have a nice day!!")
