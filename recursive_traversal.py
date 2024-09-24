def trav(lis,recursed = 1, items = 0, falls = -1):
    """Takes a list of lists of lists... and adds all the numbers in it"""
    # if num is value add to the sum otherswise recurse down the list
    sum = 0
    for i in lis:
        if type(i) == list:
            back = trav(i)
            sum += back[0]
            recursed += back[1]
            items += back[2] + 1
            if falls < back[3]:
                falls = back[3]
        elif type(i) == int or type(i) == float:
            sum += i
            items += 1 
        else:
            items += 1
    return sum, recursed, items, falls + 1

def main():
    list = [1, [2, 3], [[4], [5, [6,'i','a', 7]]], 8]
    print("Sum",trav(list)[0],"Total Recursions",trav(list)[1],"Number of Items",trav(list)[2],"Recursisve Depth",trav(list)[3])

if __name__ == "__main__":
    main()

        