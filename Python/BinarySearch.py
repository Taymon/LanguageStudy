import sys 

def binary_search(searchable, search_value):
    searchable.sort()

    print(searchable)

    l = 0
    r = len(searchable) - 1
    m = int((l + r)/2)
    f = False

    if l < r:
        while searchable[m] != search_value:
            if search_value < searchable[m]:        
                r = m - 1
            else:
                l = m + 1
            m = int((l + r)/2)

            if searchable[m] == search_value:
                f = True

            if m == 0 | m == (len(searchable) - 1):
                break
            
        if f == True:
            print("Found the value {0} at the position of {1}".format(searchable[m], m))
        else:
            print("The system could not find the value {0} in the lsit".format(search_value))
    else:
        print("Invalid list to do the binary search.")

def run():
    binary_search([1,32,13,4,25,6,17,8,9,10,15,6,2], int(sys.argv[1]))

run()