def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negative_hash = {}
    result = []
    i = 0
    while i < len(a):
        negative_hash[a[i]] = i
        i+=1

    for item in negative_hash:
        if -item in negative_hash and item > 0:
            result.append(item)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
