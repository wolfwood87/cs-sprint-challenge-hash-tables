# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_hash = {}
    result = []
    i = 0
    while i < len(files):
        file_hash[files[i]] = files[i]
        i+=1
    a = 0
    while a < len(queries):
        if a < len(files):
            if queries[a] in file_hash[files[a]]:
                result.append(file_hash[files[a]])
        a+=1
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
