def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = dict()
   
    for i in range(0, length):
        for j in range(i+1, length):
            if weights[i] + weights[j] == limit:
                result.append(j)
                result.append(i)
                return result
          
    return None
   

    

    # for index, weight in enumerate(weights):
    #     result = limit - weights[weight]

    #     if result in cache:
    #         return [cache[result], index]
    #     else:
    #         cache[result] = index

