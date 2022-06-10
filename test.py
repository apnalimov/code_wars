def count_positives_sum_negatives(arr):
    final = []
    counter = 0
    sum = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            counter += 1
        elif arr[i] < 0:
            sum += arr[i]

    final.append(counter)
    final.append(sum)
    
    if len(arr) == 0:
        final = []

    return final


print(count_positives_sum_negatives([]))