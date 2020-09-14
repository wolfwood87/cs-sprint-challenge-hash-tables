# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_hash = {}
    query_hash = {}
    result = []
    i = 0
    while i < len(files):
        file_hash[files[i]] = files[i].split("/")[-1]
        i+=1
    a = 0
    while a < len(queries):
        query_hash[queries[a]] = queries[a]
        a+=1
    for item in file_hash:
        if file_hash[item] in query_hash:
            result.append(item)
    return result



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
