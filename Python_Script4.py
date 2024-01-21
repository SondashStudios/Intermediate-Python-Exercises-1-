#Caius Iliesi
#Date: 1/21/2024

def get_sum_of_integers():
  total_sum = 0
  count = 0

  while count < 5:
      try:
          user_input = int(input(f"Enter int #{count + 1}: "))
          total_sum += user_input
          count += 1
      except ValueError:
          print("Invalid input. Please enter an int.")

  return total_sum

# Get and print the sum of 5 integers in one line
result_sum = get_sum_of_integers()
print(f"Your sum is {result_sum}", end="")