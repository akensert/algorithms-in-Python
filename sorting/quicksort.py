
def quick_sort(array, low_idx, high_idx):
    """recursive variant of quicksort, pivoting on
    the last element ('high_idx') of the (sub)arrays"""

    if low_idx < high_idx:

        pivot = array[high_idx]
        i = low_idx-1
        for j in range(low_idx, high_idx):
            if array[j] < pivot:
                i += 1
                array[j], array[i] = array[i], array[j]
        i += 1
        array[high_idx], array[i] = array[i], array[high_idx]

        quick_sort(array, low_idx, i-1)
        quick_sort(array, i+1, high_idx)

    # no need to return array as the inputted array gets sorted inplace,
    # but is returned anyways
    return array


if __name__ == '__main__':

    array = input('input a sequence of single digit integers: ')
    print('array inputted:', array)
    array = [int(i) for i in list(array)]              # make into list of ints
    sorted_array = quick_sort(array, 0, len(array)-1)
    sorted_array = ''.join(str(i) for i in sorted_array) # make into string
    print('array sorted:  ', sorted_array)
