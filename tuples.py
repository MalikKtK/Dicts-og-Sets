data_structure = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

# Create a list of tuples from data_structure with set1
list_of_tuples_set1 = [(key, data_structure[key]) for key in data_structure if key in set1]

# Create a list of tuples from data_structure with set2
list_of_tuples_set2 = [(key, data_structure[key]) for key in data_structure if key in set2]

# Print the list of tuples for set1
print("List of tuples from data_structure with set1:", list_of_tuples_set1)

# Print the list of tuples for set2
print("List of tuples from data_structure with set2:", list_of_tuples_set2)

# Create a union using set methods
union_set_method = set1.union(set2)
print("Union using set methods:", union_set_method)

# Create a union using set operators
union_set_operator = set1 | set2
print("Union using set operators:", union_set_operator)

# Create a symmetric difference using set methods
symmetric_difference_set_method = set1.symmetric_difference(set2)
print("Symmetric difference using set methods:", symmetric_difference_set_method)

# Create a symmetric difference using set operators
symmetric_difference_set_operator = set1 ^ set2
print("Symmetric difference using set operators:", symmetric_difference_set_operator)

# Create a difference using set methods
difference_set_method = set1.difference(set2)
print("Difference using set methods:", difference_set_method)

# Create a difference using set operators
difference_set_operator = set1 - set2
print("Difference using set operators:", difference_set_operator)

# Check if the sets are disjoint using set methods
are_disjoint_method = set1.isdisjoint(set2)
print("Are the sets disjoint (using set methods)?", are_disjoint_method)

# Check if the sets are disjoint using set operators
are_disjoint_operator = not (set1 & set2)
print("Are the sets disjoint (using set operators)?", are_disjoint_operator)
