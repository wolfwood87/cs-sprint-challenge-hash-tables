def get_indices_of_item_weights(weights, length, limit):
    weight_hash = {}
    dup_hash = {}
    i = 0
    while i < length:
        if weights[i] in weight_hash:
            dup_hash[weights[i]] = i
        else:
            weight_hash[weights[i]] = i
            print(weight_hash)
        i += 1
        
    for weight in weights:
        if limit - weight in weight_hash:
            if limit-weight in dup_hash:
                result = (dup_hash[limit-weight], weight_hash[weight])
                print(result)
                return result
            print(weight_hash[weight])
            print(weight_hash[limit-weight])
            result = (weight_hash[limit-weight], weight_hash[weight])
            print(result)
            return result
    return None


# weights_3 = [4, 6, 10, 15, 16]
# get_indices_of_item_weights(weights_3, 5, 21)
