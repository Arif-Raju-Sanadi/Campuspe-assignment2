#Q3


#getting sentence from user
text = input("Enter a sentence: ")

#printing same sentence
print("Original:", text)

#finding total letters with space
count_with_space = len(text)

#removing space to count without space
text_no_space = text.replace(" ", "")
count_without_space = len(text_no_space)

#breaking sentence into words
words = text.split()

#counting how many words
word_count = len(words)

#changing sentence into different cases
upper_text = text.upper()
lower_text = text.lower()
title_text = text.title()

#getting first and last word

first_word = words[0]
last_word = words[-1]


#reversing the sentence
reverse_text = text[::-1]

#showing output
print("Characters (with spaces):", count_with_space)
print("Characters (without spaces):", count_without_space)
print("Words:", word_count)
print("UPPERCASE:", upper_text)
print("lowercase:", lower_text)
print("Title Case:", title_text)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reverse_text)