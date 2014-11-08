"""
Given an array of numbers in a file (in different lines) this script return the number of inversions of the array.
An inversion is considered when a number bigger than other appears in first place
"""

def count_inv_split(array_left, array_right):
    len_left= len(array_left)
    len_right = len(array_right)
    length = len(array_left) + len(array_right)
    output_array = [0] * length
    i = 0
    j = 0
    inversions = 0
    for index in range(0, length):
        if (i < len_left) and (j < len_right):
            if array_left[i] > array_right[j]:
                output_array[index] = array_right[j]
                inversions += (len_left - i)
                j += 1
            else:
                output_array[index] = array_left[i]
                i += 1
        elif i < len_left:
            output_array[index] = array_left[i]
            i += 1
        else:
            output_array[index] = array_right[j]
            j += 1

    return output_array, inversions


def count_inv(array):
    length = len(array)
    if length == 1:
        return array, 0
    array_left, inv_left = count_inv(array[:(length/2)])
    array_right, inv_right = count_inv(array[length/2:])
    ordered_array, inv_split = count_inv_split(array_left, array_right)
    return ordered_array, inv_left + inv_right + inv_split


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process an array of numbers')
    parser.add_argument('--f', dest='file_to_parse',
        help='File to parse')

    args = parser.parse_args()

    with open(args.file_to_parse, 'r') as f:
        input = f.read()
        elements = input.split('\r\n')
        elements = map(lambda x: int(x),filter(lambda x: x.isdigit(), elements))
        final_result = count_inv(elements)
        print "Final result is ...."
        print final_result[1]
