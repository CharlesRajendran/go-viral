def readFile():
    
    fh = open("movie_ids.txt","r")
    lines = fh.readlines()
    fh.close()

    ids = []
    for line in lines:
        ids.append(line[:-2])

    return ids

