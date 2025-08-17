import random

# ==============================
# 📚 Rule-Based Book Recommendation System
# ==============================

"""
This system recommends books based on simple IF–ELSE style rules.
User inputs:
- Genre
- Mood
- Preferred Length
- Age Group
- Reading Purpose

System returns:
- A random book from the matching rule set.
"""

print("📚 Welcome to the Rule-Based Book Recommendation System!")
print("Answer the following questions to get a book suggestion.")
print("Type 'q' at any time to quit.\n")

# ==============================
# RULE DEFINITIONS
# ==============================
# Each rule describes: genre + mood + length + age group + purpose
# → Corresponding list of books that match that rule
rules = [
    # --- Fantasy ---
    {
        "genre": "fantasy",
        "mood": "adventurous",
        "length": "long",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "The Lord of the Rings by J.R.R. Tolkien",
            "A Song of Ice and Fire by George R.R. Martin",
            "The Wheel of Time by Robert Jordan"
        ]
    },
    {
        "genre": "fantasy",
        "mood": "relaxing",
        "length": "short",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "The Ocean at the End of the Lane by Neil Gaiman",
            "Stardust by Neil Gaiman"
        ]
    },
    {
        "genre": "fantasy",
        "mood": "adventurous",
        "length": "medium",
        "age_group": "young adult",
        "purpose": "entertainment",
        "books": [
            "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
            "Percy Jackson and the Olympians by Rick Riordan"
        ]
    },

    # --- Mystery ---
    {
        "genre": "mystery",
        "mood": "suspenseful",
        "length": "medium",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "The Da Vinci Code by Dan Brown",
            "Gone Girl by Gillian Flynn",
            "The Girl with the Dragon Tattoo by Stieg Larsson"
        ]
    },
    {
        "genre": "mystery",
        "mood": "suspenseful",
        "length": "short",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "And Then There Were None by Agatha Christie",
            "Murder on the Orient Express by Agatha Christie"
        ]
    },

    # --- Romance ---
    {
        "genre": "romance",
        "mood": "emotional",
        "length": "medium",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "The Notebook by Nicholas Sparks",
            "Pride and Prejudice by Jane Austen"
        ]
    },
    {
        "genre": "romance",
        "mood": "relaxing",
        "length": "short",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "Eleanor & Park by Rainbow Rowell",
            "Attachments by Rainbow Rowell"
        ]
    },

    # --- Sci-Fi ---
    {
        "genre": "sci-fi",
        "mood": "inspiring",
        "length": "short",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "The Martian by Andy Weir",
            "I, Robot by Isaac Asimov",
            "Ender's Game by Orson Scott Card"
        ]
    },
    {
        "genre": "sci-fi",
        "mood": "adventurous",
        "length": "medium",
        "age_group": "adult",
        "purpose": "entertainment",
        "books": [
            "Dune by Frank Herbert",
            "Foundation by Isaac Asimov"
        ]
    },

    # --- Non-Fiction ---
    {
        "genre": "non-fiction",
        "mood": "inspiring",
        "length": "medium",
        "age_group": "adult",
        "purpose": "motivation",
        "books": [
            "Atomic Habits by James Clear",
            "The 7 Habits of Highly Effective People by Stephen R. Covey"
        ]
    },
    {
        "genre": "non-fiction",
        "mood": "learning",
        "length": "long",
        "age_group": "adult",
        "purpose": "learning",
        "books": [
            "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
            "Educated by Tara Westover"
        ]
    },

    # --- Children's ---
    {
        "genre": "fantasy",
        "mood": "adventurous",
        "length": "short",
        "age_group": "children",
        "purpose": "entertainment",
        "books": [
            "The Gruffalo by Julia Donaldson",
            "Where the Wild Things Are by Maurice Sendak"
        ]
    },
    {
        "genre": "non-fiction",
        "mood": "learning",
        "length": "short",
        "age_group": "children",
        "purpose": "learning",
        "books": [
            "National Geographic Kids Almanac",
            "DK Eyewitness: Animal"
        ]
    },

    # --- YA Non-Fiction ---
    {
        "genre": "non-fiction",
        "mood": "inspiring",
        "length": "medium",
        "age_group": "young adult",
        "purpose": "motivation",
        "books": [
            "I Am Malala by Malala Yousafzai",
            "The Diary of a Young Girl by Anne Frank"
        ]
    }
]

# ==============================
# MAIN LOOP
# ==============================
while True:
    # --- Gather User Input ---
    genre = input("\nChoose a genre (fantasy, mystery, romance, sci-fi, non-fiction) or 'q' to quit: ").strip().lower()
    if genre in ["q", "quit"]:
        print("👋 Goodbye!")
        break

    mood = input("Choose a mood (adventurous, relaxing, emotional, inspiring, suspenseful) or 'q' to quit: ").strip().lower()
    if mood in ["q", "quit"]:
        print("👋 Goodbye!")
        break

    length = input("Preferred length? (short, medium, long) or 'q' to quit: ").strip().lower()
    if length in ["q", "quit"]:
        print("👋 Goodbye!")
        break

    age_group = input("Age group? (children, young adult, adult) or 'q' to quit: ").strip().lower()
    if age_group in ["q", "quit"]:
        print("👋 Goodbye!")
        break

    purpose = input("Reading purpose? (entertainment, learning, motivation) or 'q' to quit: ").strip().lower()
    if purpose in ["q", "quit"]:
        print("👋 Goodbye!")
        break

    # --- Match Rules ---
    matching_books = [
        r["books"] for r in rules
        if r["genre"] == genre
        and r["mood"] == mood
        and r["length"] == length
        and r["age_group"] == age_group
        and r["purpose"] == purpose
    ]

    # --- Show Recommendation ---
    if matching_books:
        # Flatten list of books and choose a random one
        flat_books = [book for sublist in matching_books for book in sublist]
        recommendation = random.choice(flat_books)
        print("\n✅ We recommend you read:", recommendation)
    else:
        print("\n⚠️ Sorry, no exact matches found. Try adjusting your preferences.")


