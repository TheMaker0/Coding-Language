 
noun1 = input("Enter first noun: ")
noun2 = input("Enter second noun: ")
noun3 = input("Enter third noun: ")

adjective1 = input("Enter first adjective: ")
adjective2 = input("Enter second adjective: ")
adjective3 = input("Enter third adjective: ")

lyrics = "I thought my HEART had learned its lesson (ooh)\nIt feels so GOOD when you START out (ooh)\nMy head is SCREAMING, 'Get a GRIP, GIRL!' (Ahh)\nUnless you're DYING to CRY your Heart out"

replaceLyrics = lyrics.replace("HEART", noun1.upper()).replace("GOOD", noun2.upper()).replace("START", noun3.upper()).replace("SCREAMING", adjective1.upper()).replace("GIRL", adjective2.upper()).replace("DYING", adjective3.upper())

print("\nOriginal Lyrics:")
print(lyrics)
print("\nReplaced Lyrics:")
print(replaceLyrics)
