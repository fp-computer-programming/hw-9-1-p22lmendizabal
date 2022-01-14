#author: LM (AMDG) 1/13/22
def odd_numbers(lst):
    for index, value in enumerate(lst):
        if value % 2 != 0:
            print(index, value)

print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17, 21]))