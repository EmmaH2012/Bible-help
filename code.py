# Bible Help Program

# Ask the user for a problem/topic
problem = input("Please enter problem or topic: ").strip().lower()

# Check if the input matches "anxiety"
if problem == "anxiety":
    print(
        "In the Bible it says: "
        "'Do not be anxious about anything, but in every situation, "
        "by prayer and petition with thanksgiving, present your requests to God.' "
        "- Philippians 4:6"
    )
else:
    print("Sorry, I don't have a verse for that topic yet.")




