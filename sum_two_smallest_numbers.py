def sum_two_smallest_numbers(numbers):
    numbers.sort()
    final = 0
    final += numbers[0]
    final += numbers[1]

    return final

print(sum_two_smallest_numbers([18, 8, 5, 12, 22]))