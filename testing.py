def sum_combinations_with_sources(list1, list2, list3, list4):
    result = []
    for i, a in enumerate(list1):
        for j, b in enumerate(list2):
            for k, c in enumerate(list3):
                for l, d in enumerate(list4):
                    total_sum = a + b + c + d
                    description = f"Sum: {total_sum} (genre: {a}, director: {
                        b}, cast: {c}, rating: {d})"
                    result.append((total_sum, description))
    return result


def search_sum(result_list, target_sum):
    matches = [item[1] for item in result_list if item[0] == target_sum]
    return matches if matches else [f"No results found for sum: {target_sum}"]


# Example usage
list1 = [1, 3, 5]
list2 = [1, 3]
list3 = [1, 3, 5]
list4 = [1, 2, 4]

sums_with_sources = sum_combinations_with_sources(list1, list2, list3, list4)

# Search for a specific result
target = 8
matches = search_sum(sums_with_sources, target)
for match in matches:
    print(match)

target = 11
matches = search_sum(sums_with_sources, target)
for match in matches:
    print(match)

print()
sums_with_sources.sort()
for sum in sums_with_sources:
    print(sum)
