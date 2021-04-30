
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


if __name__ == '__main__':

    array = input('input a sequence of single digit integers: ')
    print('array inputted:', array)
    array = [int(i) for i in list(array)]             # make into list of ints
    sorted_array = bubble_sort(array)
    sorted_array = ''.join(str(i) for i in sorted_array) # make into string
    print('array sorted:  ', sorted_array)
