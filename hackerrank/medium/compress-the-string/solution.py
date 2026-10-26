from itertools import groupby

my_string = input()

result_list = []

for character, group in groupby(my_string):
    occurrences = list(group)
    count = len(occurrences)
    number = int(character)
    
    result_list.append((count, number))

print(*result_list)
