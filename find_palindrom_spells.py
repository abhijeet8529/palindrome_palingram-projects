# import mydictionary
# wordl = mydictionary.load('dictionary.txt') 
# palindrom = []   
# for word in wordl:
#     if len(word)> 1 and word == word[::-1]:
#         palindrom.append(word)
        
# print("\nThe numbers of palindrome found is : ",len(palindrom))
# print(*palindrom,sep='\n')
# List of words
import mydictionary
word_list = mydictionary.load('dictionary.txt')
print(f"Loaded {len(word_list)} words from dictionary.txt")
pali_list = []

# Iterate through each word in the list
for word in word_list:
    end = len(word)
    rev_word = word[::-1]
    
    # Check if the word is more than one character long
    if end > 1:
        # Iterate through each position of the word
        for i in range(end):
            # Check for palingrams
            if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                print(f"Found palingram: {word} {rev_word[end-i:]}")
                pali_list.append((word, rev_word[end-i:]))
            
            if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                print(f"Found palingram: {rev_word[:end-i]} {word}")
                pali_list.append((rev_word[:end-i], word))

# Print palingrams
if pali_list:
    print("\nFound Palingrams:")
    for first, second in pali_list:
        print(f"{first} {second}")
else:
    print("No palingrams found.")
