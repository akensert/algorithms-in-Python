
def counting_sort(array):

    max_index = max(array)+1

    counts = [0] * max_index

    # step 1. count occurences for each integer
    for a in array:
        counts[a] += 1

    # step 2. compute cumulative sum
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # step 3. Add each element in array to correct index
    #         in output array, based on counts array
    output = [0] * len(array)
    for a in array:
        output[counts[a]-1] = a
        counts[a] -= 1

    return output


if __name__ == '__main__':

    array = input('input a sequence of single digit integers: ')
    print('array inputted:', array)
    array = [int(i) for i in list(array)]              # make into list of ints
    sorted_array = counting_sort(array)
    sorted_array = ''.join(str(i) for i in sorted_array) # make into string
    print('array sorted:  ', sorted_array)
