review_ids = []

#read_file('data/test/urls_neg.txt')

def read_file(file):
    ids = []
    file_handler = open(file,'r')
    document_lines = list(set(file_handler.readlines()))
    file_handler.close()
    
    for line in document_lines:
        ids.append(line.split('/')[4])

    return ids


def return_ids():
    review_ids =read_file('data/test/urls_pos.txt') + read_file('data/test/urls_neg.txt')+ read_file('data/train/urls_pos.txt') + read_file('data/train/urls_neg.txt')
    return list(set(review_ids))

def write_file_ids(ids):
    try:
        file_h = open('movie_ids.txt','a')

        for id in ids:
            file_h.write(id+"\n")

        file_h.close()
    
        return "done!"

    except Exception as e:
        print(e)

write_file_ids(return_ids())
