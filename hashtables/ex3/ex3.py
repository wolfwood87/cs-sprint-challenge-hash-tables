def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    array_hash = {}
    result = []
    for array in arrays:
        for item in array:
            if item in array_hash:
                array_hash[item] += 1
            else:
                array_hash[item] = 1
    for array in array_hash:
        if array_hash[array] == len(arrays):
            result.append(array)
    print(result)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
