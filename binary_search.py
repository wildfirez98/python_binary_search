def binary_search(data, el):
    first = 0
    last = len(data)-1 # Note that last = len(data)-1 because indexing starts at 0.
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else: 
            if el < data[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))
