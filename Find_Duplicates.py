# Function to find duplicates in a list

some_list = ['a', 'b', 'c', 'd', 'b', 'n', 'n', 'a', 'f', 'r', 'a']
another_list = [1, 3, 6, 2, 6, 1, 2, 3, 5, 6, 7, 3, 1, 3, 8, 4, 8, 24, 14, 2, 12, 13, 13, 14, 7, 3, 4]


def find_duplicates(x):
    dups = []
    for value in x:
        if x.count(value) > 1 and value not in dups:
            dups.append(value)
    return dups


print(find_duplicates(some_list))
print(find_duplicates(another_list))
