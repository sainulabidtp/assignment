import random
import math



def split(items, ratios):
    # Calculate the total number of elements
    total_elements = sum(ratios)

    # Calculate the number of elements for each sublist
    num_elements = [math.floor(len(items) * ratio / total_elements) for ratio in ratios]

    # Calculate the remaining elements after flooring
    remaining_elements = len(items) - sum(num_elements)

    # Assign the remaining elements to the sublists in a round-robin fashion
    for i in range(remaining_elements):
        num_elements[i % len(num_elements)] += 1

    # Shuffle the items
    random.shuffle(items)

    # Split the items into sublists based on the calculated sizes
    result = []
    start_index = 0
    for num in num_elements:
        result.append(items[start_index:start_index + num])
        start_index += num

    return result
#items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# = [50, 40, 10]

n = int(input("Enter the number of elements: "))
items = []  # Empty list to store the items

for i in range(n):
    num = int(input("Enter a number: "))
    items.append(num)  # Add the item to the list

print("The numbers entered are:", items)

r = int(input("Enter the number of ratios: "))


ratios = []  # Empty list to store the ratios

for i in range(r):
    ratio = int(input("Enter a number: "))
    ratios.append(ratio)  # Add the ratios to the list

print("The numbers entered are:", ratios)




result = split(items, ratios)
print(result)


