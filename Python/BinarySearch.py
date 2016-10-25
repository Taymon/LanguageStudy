import sys 

def binary_search(searchable, search_value):
    searchable.sort()

    l = 0
    r = len(searchable) - 1
    m = int((l + r)/2)

    while searchable[m] != search_value:
        if search_value < searchable[m]:        
            r = m
        else:
            l = m
        m = int((l + r)/2)
        
    print("Found the value: {0} at the position of {1}".format(searchable[m], m))

def run():
    binary_search([1,32,13,4,25,6,17,8,9,10,15,6,2], int(sys.argv[1]))

run()