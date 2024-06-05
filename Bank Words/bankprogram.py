print()
print("     |   Welcome to Bank Program     |   ")
word_bank = []
while True:
 
    print("_____________________________________________")
    word = input("Enter a word: ")
    word_bank.append(word)
    print("_____________________________________________")
    try_again = input("Do you want to enter another word? (y/n): ")
    print("_____________________________________________")
    if try_again.lower() == 'n':
        break

print("_____________________________________________")
print("TOTAL NUMBERS OF WORD ENTERED:", len(word_bank))
print("\n_____________________________________________")
print("     |   WORD ENTERED    |   \n")

for word in word_bank:
    print(word)
