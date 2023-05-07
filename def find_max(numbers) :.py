def find_max(numbers) :
    max_num = numbers[0]
    for num in numbers :
        if num > max_num:
            max_num = num

    return max_num

numbers = [5, 8, 2, 10, 3]
result = find_max(numbers)
print ("naibolshee", result)
