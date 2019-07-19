"""
Pig Latin is an argot ("secret" language) in which words in English are altered to conceal the words from others not familiar with the rules.

You convert a word to pig latin by transferring the initial consonant or consonant cluster of the word to the end of the word with -ay appended to the end.
If the word starts with a vowel (including y), append -yay to the end. For example, "pig" would become igpay (taking the 'p' and 'ay' to create a suffix).

Examples:
Input: say
Output: aysay

Input: english
Output: englishyay

Input: smile
Output: ilesmay

Write a program that translates the user input (an English word) to Pig Latin.
"""

vowels = ["a", "e", "i", "o", "u", "y"]

myword = input("Enter a word: \n")

word = myword.lower()

if word[0] in vowels and word.isalpha():
    new_word = word + "yay"
    print(f"{myword} ==> {new_word}")

elif word[0] not in vowels and word.isalpha():
    word_list = []

    for letter in word:
        if letter not in vowels:
            word_list.append(letter)
            word = word[1:len(word)]
            
        elif letter in vowels:
            break
            
    word = "".join(word)
    word_list = "".join(word_list)
    new_word = word + word_list + "ay"
    print(f"{myword} ==> {new_word}")

else:
    print("That is not a valid word.")
