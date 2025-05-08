import json
import os
from time import sleep
from datetime import datetime

# Log File
LOG_FILE = "logs.json"

def load_achievements():
    """Load achievements from logs.json."""
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        return []

def save_achievements(achievements):
    """Save achievements to log.json."""
    with open(LOG_FILE, 'w') as file:
        json.dump(achievements, file, indent=4)

def add_achievement(title, note):
    """Add a new achievement with title, note, and timestamp."""
    achievements = load_achievements()
    achievement_id = max([a['id'] for a in achievements], default=0) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:$S")
    new_achievement = {
            "id": achievement_id,
            "title": title,
            "note": note,
            "timestamp": timestamp
    }
    achievements.append(new_achievement)
    save_achievements(achievements)
    print(f"Achievement '{title} added successfully!")

def show_achievements():
    """Show all achievements"""
    achievements = load_achievements()
    if not achievements:
        sleep(.4)
        print("\nNo achievements found.\n")
        return
    for a in achievements:
        print(f"ID: {a['id']}, Title: {a['title']}, Timestamp: {a['timestamp']}")
        print(f"Note: {a['note']}\n")

def main():
    """Main Program Loop"""
    while True:
        sleep(.3)
        print("\n- Accomplishment Log -\n")
        print("(A)dd Achievement")
        sleep(.3)
        print("(S)how Achievements")
        sleep(.3)
        print("(E)xit")
        sleep(.3)
        choice = input("\nEnter your choice: ")

        if choice == 'A' or choice == 'a':
            title = input("Achievement Title: ")
            note = input("Note: ")
            add_achievement(title, note)
        elif choice == 'S' or choice == 's':
            show_achievements()
        elif choice == 'E' or choice =='e':
            print("\nHave a nice day!")
            sleep(.5)
            print("\nRemember, you can achieve anything!\n")
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()
