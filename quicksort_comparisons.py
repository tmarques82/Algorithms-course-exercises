"""
Algorithm used for computing the number of comparisons needed when sorting an array number from a file with quicksort
algorithm. Pivots can be selected in different ways (default one is the first element of the array)
"""

def get_median_pivot(init_array):
    if len(init_array) < 3:
        return 0
    middle_index = int(len(init_array)/2 -1 + len(init_array)%2)
    first_element = init_array[0]
    last_element = init_array[-1]
    middle_element = init_array[middle_index]
    min_val = min([first_element, last_element, middle_element])
    max_val = max([first_element, last_element, middle_element])
    if first_element not in (min_val, max_val):
        return 0
    if last_element not in (min_val, max_val):
        return len(init_array) - 1
    if middle_element not in (min_val, max_val):
        return middle_index


def choose_pivot_index(init_array):
    """
    3 different pivots for each exercise: first element, last element and medium-of-three
    """
    #return get_median_pivot(init_array)
    #return len(init_array) -1
    return 0


def swap_elems(init_array, index_1, index_2):
    aux = init_array[index_1]
    init_array[index_1] = init_array[index_2]
    init_array[index_2] = aux


def quicksort(init_array):
    len_array = len(init_array)
    if len_array == 1:
        return init_array, 0
    pivot_index = choose_pivot_index(init_array)
    pivot_element = init_array[pivot_index]
    if pivot_index:
        swap_elems(init_array, pivot_index, 0)
    i = 1
    j = 1
    comparisons = 0

    for index in range(j, len_array):
        comparisons += 1
        if init_array[index] < pivot_element:
            if i != j:
                swap_elems(init_array, i, j)
            i += 1
        j += 1
    swap_elems(init_array, 0, i-1)
    first_part = []
    second_part = []
    left_comparisons = 0
    right_comparisons = 0
    if i > 1:
        first_part, left_comparisons = quicksort(init_array[:i-1])
    if i != len_array:
        second_part, right_comparisons = quicksort(init_array[i:])
    final_array = first_part + [pivot_element] + second_part
    return final_array, comparisons + left_comparisons + right_comparisons


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a file with an array to be sorted with quicksort algorithm')
    parser.add_argument('--f', dest='file_to_parse',
        help='File to parse')

    args = parser.parse_args()

    with open(args.file_to_parse, 'r') as f:
        input = f.read()
        elements = input.split('\r\n')
        elements = map(lambda x: int(x),filter(lambda x: x.isdigit(), elements))

    a = quicksort(elements)
    print a[0]
