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
    ) choice = input("Would you like a Bible study about anxiety? (please type Y or N): ").strip().lower()
    if choice == "Y":
         print('Sorry, this feature isnt avalible yet please try again later!')
elif choice == "N":
     print('Ok! I hope this helped!')
else:
    print("Sorry, I don't have a verse for that topic yet! Please try again later or check spelling.")




