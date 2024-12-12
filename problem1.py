def sum_even_numbers(nums):
    for number in nums:
        if number % 2 != 0:
            nums.pop(number)
    for number in nums:
        last = 0
        last = last + number