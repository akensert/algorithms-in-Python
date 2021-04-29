
def merge_sort(array):
    """recursive variant of mergesort"""

    if len(array) == 1:
        return array

    center_idx = len(array)//2

    left_array = merge_sort(array[:center_idx])
    right_array = merge_sort(array[center_idx:])

    merged_sorted_array = []
    i, j = 0, 0
    while True:
        if left_array[i] >= right_array[j]:
            merged_sorted_array.append(right_array[j])
            j += 1
            if j == len(right_array):
                merged_sorted_array.extend(left_array[i:])
                break
        else:
            merged_sorted_array.append(left_array[i])
            i += 1
            if i == len(left_array):
                merged_sorted_array.extend(right_array[j:])
                break

    return merged_sorted_array


if __name__ == '__main__':

    array = input('input a sequence of single digit integers: ')
    print('array inputted:', array)
    array = [int(i) for i in list(array)]             # make into list of ints
    sorted_array = merge_sort(array)
    sorted_array = ''.join(str(i) for i in sorted_array) # make into string
    print('array sorted:  ', sorted_array)
