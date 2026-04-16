import random

items = {
    "movies": ["action movie", "comedy movie", "horror movie", "romantic movie"],
    "books": ["science book", "story book", "history book", "fiction book"],
    "music": ["pop music", "rock music", "classical music", "jazz music"]
}

user_category = input("Enter category: ").lower()
user_preference = input("Enter interest: ").lower()

if user_category in items:
    matched = [item for item in items[user_category] if user_preference in item]

    if matched:
        print("\n🎯 Recommended:")
        print(random.choice(matched))
    else:
        print("\n⚡ Try this instead:")
        print(random.choice(items[user_category]))
else:
    print("Invalid category")