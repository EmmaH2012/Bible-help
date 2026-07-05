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

    # Ask follow-up question
    choice = input("Would you like a Bible study about anxiety? (please type Y or N): ").strip().lower()

    if choice == "y":
        print("Sorry, this feature isn't available yet. Please try again later!")
    elif choice == "n":
        print("Ok! I hope this helped!")
    else:
        print("I didn't understand your answer. Please type Y or N.")

else:
    print("Sorry, I don't have a verse for that topic yet! Please try again later or check spelling.")
    if problem == "doubt":
        print(
            "In the Bible it says: "
            "'But when you ask, you must believe and not doubt,"
            "because the one who doubts is like a wave of the sea,"
            "blown and tossed by the wind.'"
            "- James 1:6"

        )
        if choice == "y":
        print("Sorry, this feature isn't available yet. Please try again later!")
    elif choice == "n":
        print("Ok! I hope this helped!")
    else:
        print("I didn't understand your answer. Please type Y or N.")







