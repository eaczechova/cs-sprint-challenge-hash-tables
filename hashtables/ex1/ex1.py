def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    for i in range(0, length):
        for j in range(i+1, length):
            if weights[i] + weights[j] == limit:
                result.append(j)
                result.append(i)
                return result
    return None


# to store 