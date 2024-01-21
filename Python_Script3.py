#Caius Iliesi
#Date: 1/21/2024

def get_letter_count(input_string):
  letter_count = {}
  for char in input_string:
      if char.isalpha():
          char_lower = char.lower()
          letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
  return letter_count

# Take input from the user
user_input = input("Enter a string: ")

# Get and print the letter count in one line
print(get_letter_count(user_input), end="")