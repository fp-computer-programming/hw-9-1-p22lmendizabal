#author: LM (AMDG) 1/9/22
def even_number(lst):
    for index, value in enumerate(lst):
        if index % 2 == 0:
            print(value)
            
            
print(even_number(['me', 'you', 6, 8, 3, 33, 1, 9, 7, 5, 2]))
