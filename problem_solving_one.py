# Problem Solving Problems Part 1

# To be a good problem solver, it is important to be able to break problems down.

# One way to go about this is to write out the steps it will take to solve the problem.

# These steps are written down in Plain English in a manner that are easily explainable to someone who may not be technical. The idea is that in order to code something out, 
# you first need to have a good understanding of what it is you are attempting to solve.

# For each of the four problem solving problems below, write out the steps it will take to go about solving the problem. For example, once you are done writing 
# out the steps for the “reverse a string” problem, you would then write out the code to solve the problem. You would then repeat the process for each ensuing problem. 
# Ideally, this will be a good habit that you will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.

# Problems

# 1. Reverse a string

# a. Write code that takes a string as input and returns the string reversed

# b. i.e. “Hello” will be returned as “olleH”

# 2. Capitalize letter

# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

# 3. Compress a string of characters

# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

# 4. BONUS CHALLENGE: Palindrome

# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result



# 1. Reverse a string
# Slice

def backwards_man(x):
  return x[: : -1]

user_word = backwards_man(input("Input a word or phrase you'd like to see backwards!: "))

print(user_word)

# Or no frills

def reverse(text):
    user_text = ""
    word = len(text) - 1

    while word >= 0:
        user_text += text[word]
        word -= 1

    return user_text

print(reverse(input("Input another word or phrase you'd like to see backwards!: ")))


# 2. Capitalize letter
# import string and use .capwords

import string

cap_first_letter = string.capwords(input("Enter a phrase: "))
print(cap_first_letter)

# Or use .upper and .split

# create a string
try_two = input("Enter another phrase: ")
# capitalize first letter of each word
caps_output = " ".join(word[0].upper()+word[1:] for word in try_two.split(" "))
print(caps_output)

# 3 Compress a string of characters

def solve(to_compress):
   character = ""
   counter = 1
   for i in range(1, len(to_compress)):
      if to_compress[i - 1] == to_compress[i]:
         counter += 1
      else:
         character = character + to_compress[i - 1]
         if counter > 1:
            character += str(counter)
         counter = 1
   character = character + to_compress[-1]
   if counter > 1:
      character += str(counter)
   return character

to_compress = input("Please enter random alphabet characters: ")
print(solve(to_compress))