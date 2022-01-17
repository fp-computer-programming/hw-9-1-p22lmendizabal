# author: LM (AMDG) 1/14/22

def find_thing(item, search):
    for index, value in enumerate(item):
        if value == search[0]:
            mark = index
            check = ''
            for x in range(len(search)):
                check += item[mark]
                mark += 1
                if check == search:
                    return index
    return -1



print(find_thing("apple", "ple"))
