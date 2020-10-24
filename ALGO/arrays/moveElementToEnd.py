# O(N)  O(1)
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        # [2, 1, 3, 2, 4, 2, 2,2] right pointer move until to 4
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

