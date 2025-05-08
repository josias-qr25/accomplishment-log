import json
import os
from time import sleep
from datetime import datetime

# Log File
LOG_FILE = "logs.json"

def load_accomplishments():
    """Load accomplishments from logs.json."""
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        return []

def save_accomplishment(accomplishments):
    """Save accomplishments to log.json."""
    with open(LOG_FILE, 'w') as file:
        json.dump(accomplishments, file, indent=4)

def add_accomplishment(title, note):
    """Add a new accomplishment with title, note, and timestamp."""
    accomplishments = load_accomplishments()
    accomplishment_id = max([a['id'] for a in accomplishments], default=0) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:$S")
    new_accomplishment = {
            "id": accomplishment_id,
            "title": title,
            "note": note,
            "timestamp": timestamp
    }
    accomplishments.append(new_accomplishment)
    save_accomplishment(accomplishments)
    print(f"Accomplishment '{title} added successfully!")

def show_accomplishments():
    """Show all accomplishments."""
    accomplishments = load_accomplishments()
    if not accomplishments:
        sleep(.4)
        print("\nNo accomplishments found.\n")
        return
    for a in accomplishments:
        print(f"ID: {a['id']}, Title: {a['title']}, Timestamp: {a['timestamp']}")
        print(f"Note: {a['note']}\n")

def main():
    """Main Program Loop"""
    while True:
        sleep(.3)
        print("\n- Accomplishment Log -\n")
        print("(A)dd Accomplishment")
        sleep(.3)
        print("(S)how Accomplishment")
        sleep(.3)
        print("(E)xit")
        sleep(.3)
        choice = input("\nEnter your choice: ")

        if choice == 'A' or choice == 'a':
            title = input("Accomplishment Title: ")
            note = input("Note: ")
            add_accomplishment(title, note)
        elif choice == 'S' or choice == 's':
            show_accomplishments()
        elif choice == 'E' or choice =='e':
            print("\nHave a nice day!")
            sleep(.5)
            print("\nRemember, you can accomplish anything!\n")
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()
