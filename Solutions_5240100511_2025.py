#Question 1
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)
#Question 2
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = [part[0].upper() for part in name_parts]
print("Initials:", ".".join(initials) + ".")
#Question 3
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
#Question 4
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)
#Question 5
string = "This is a string and it is an example."
modified_string = string.replace("is", "was")
print("Modified String:", modified_string)
