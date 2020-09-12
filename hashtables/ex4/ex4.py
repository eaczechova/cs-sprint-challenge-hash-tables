def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for number in a:
        if number > 0 and number not in cache:
            cache[number] = 0
      
    for neg_num in a:
        if neg_num < 0 and (neg_num * -1) in cache:
            cache[neg_num * -1] += 1

    for (key, value) in cache.items():
        if value >= 1:
            result.append(key)
    return result
   


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
