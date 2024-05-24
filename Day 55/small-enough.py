def small_enough(array, limit):
    return all(number <= limit for number in array)