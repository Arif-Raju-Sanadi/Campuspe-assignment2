#Q17 Palindrome Checker

#taking input from user
text=input("Enter word/number: ")

#showing original
print("Original:",text)

#converting to lower for checking
low_text=text.lower()

#reversing the text
rev_text=low_text[::-1]

#showing reversed
print("Reversed:",rev_text)

#checking palindrome
if low_text==rev_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")