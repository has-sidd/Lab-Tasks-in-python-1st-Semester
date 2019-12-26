word = input("Enter a Word : ")
word1 = word.lower()
vowel = 0
const = 0
for x in range(0, len(word1)):
    let = word1[x]
    if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
        vowel = vowel + 1
    else:
        const = const + 1
print("Number of Vowels are : ", vowel)
print("Number of Consonants are : ", const)