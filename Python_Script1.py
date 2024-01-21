#Caius Iliesi
#Date: 1/21/2024

def get_unique_list(input_list):
  unique_list = list(set(input_list))
  return unique_list

# Sample test list
my_list = [1, 2, 3, 2, 1, 4]

# Get and print the unique list
unique_list = get_unique_list(my_list)
print(unique_list)