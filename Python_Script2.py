#Caius Iliesi
#Date: 1/21/2024


def get_combined_dict(dict1, dict2):
  combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in sorted(set(dict1) & set(dict2))}
  return combined_dict

# Sample test dictionaries
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

# Get and print the combined dict with single quotes
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
formatted_combined_dict = str(combined_dict).replace('"', "'")
print(formatted_combined_dict, end="")