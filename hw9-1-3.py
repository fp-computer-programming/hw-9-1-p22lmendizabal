#author: LM (AMDG) 1/14/22

def find_thing(lst):
    i = 0
    user_find = str(input("Enter the substring or element you want to find: "))
    for element in str(lst):
        if user_find in element:
            element = lst.index(user_find)
            print("The index of {0} is:{1}".format(user_find, element))
        else:
            print(-1)
            break
        


find_thing([7, 8, 9, 10])