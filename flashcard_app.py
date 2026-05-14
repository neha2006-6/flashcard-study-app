import json
import os
import random

CARDS_FILE = "flashcards.json"

def load_cards():
    if os.path.exists(CARDS_FILE):
        with open(CARDS_FILE, "r") as f:
            return json.load(f)
    return []

def save_cards(cards):
    with open(CARDS_FILE, "w") as f:
        json.dump(cards, f)

def add_card():
    print("\n Add New Flashcard")
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    cards = load_cards()
    cards.append({"question": question, "answer": answer})
    save_cards(cards)
    print(" Flashcard added successfully!")

def view_cards():
    cards = load_cards()
    if not cards:
        print("\n No flashcards found!")
        return
    print("\n All Flashcards:")
    print("=" * 40)
    for i, card in enumerate(cards, 1):
        print(f"{i}. Q: {card['question']}")
        print(f"   A: {card['answer']}")
        print("-" * 40)

def study_mode():
    cards = load_cards()
    if not cards:
        print("\n❌ No flashcards to study!")
        return
    
    random.shuffle(cards)
    score = 0
    total = len(cards)
    
    print("\n Study Mode Started!")
    print(f"Total cards: {total}")
    print("=" * 40)
    
    for card in cards:
        print(f"\n Question: {card['question']}")
        input("Press Enter to see answer...")
        print(f" Answer: {card['answer']}")
        know = input("Did you know it? (y/n): ")
        if know.lower() == 'y':
            score += 1
    
    print("\n" + "=" * 40)
    print(f" Your Score: {score}/{total}")
    percentage = (score/total) * 100
    print(f" Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print(" Excellent! Keep it up!")
    elif percentage >= 60:
        print(" Good job! Keep studying!")
    else:
        print(" Keep practicing! You can do it!")

def delete_card():
    cards = load_cards()
    if not cards:
        print("\n No flashcards to delete!")
        return
    view_cards()
    try:
        index = int(input("\nEnter card number to delete: ")) - 1
        if 0 <= index < len(cards):
            deleted = cards.pop(index)
            save_cards(cards)
            print(f" Deleted: {deleted['question']}")
        else:
            print(" Invalid number!")
    except ValueError:
        print(" Please enter a valid number!")

def main():
    print("=" * 40)
    print("    Flashcard Study App")
    print("=" * 40)
    
    while True:
        print("\n1. Add Flashcard")
        print("2. View All Flashcards")
        print("3. Study Mode")
        print("4. Delete Flashcard")
        print("5. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            add_card()
        elif choice == "2":
            view_cards()
        elif choice == "3":
            study_mode()
        elif choice == "4":
            delete_card()
        elif choice == "5":
            print("\nGoodbye! Keep studying! ")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
