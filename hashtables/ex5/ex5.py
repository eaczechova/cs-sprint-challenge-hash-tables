# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # Your code here
    for f in files:
        #split path using "/" and assign last item of the list
        path = f.split("/")[-1]
        print("path", path)
        # if file not in dict create key and assign value of list with matching path
        if path not in cache:
            cache[path] = []
            cache[path].append(f)
        # if file not in dict add anothe path to the list
        else: 
            cache[path].append(f)

    for q in queries:
        if q in cache:
            result.extend(cache[q])
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
