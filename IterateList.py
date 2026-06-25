sample_list = [20, 10, 15, 10, 20, 30, 15, 35, 20]

# Create an empty dictionary
count_dict = {}

# Iterate through the list
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Display the dictionary
print("Element counts:")
print(count_dict)