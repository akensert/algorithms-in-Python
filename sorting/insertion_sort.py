
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in reversed(range(-1, i)):
            if (array[j] < array[i]):
                break
        # make insertion only if the inner loop
        # didn't break after first iteration
        if j < (i-1):
            array.insert(j+1, array.pop(i))
    return array


if __name__ == '__main__':

    array = input('input a sequence of single digit integers: ')
    print('array inputted:', array)
    array = [int(i) for i in list(array)]             # make into list of ints
    sorted_array = insertion_sort(array)
    sorted_array = ''.join(str(i) for i in sorted_array) # make into string
    print('array sorted:  ', sorted_array)
