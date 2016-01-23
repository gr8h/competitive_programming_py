def get_max_LIS(arr):

    before_max_arr = [1 for i in xrange(len(arr))]
    for i in xrange(len(arr)):
        for j in xrange(i):
            if arr[j] < arr[i] and before_max_arr[i] < before_max_arr[j] + 1:
                before_max_arr[i] = before_max_arr[j] + 1

    max_count = 1
    for count in before_max_arr:
        if count > max_count:
            max_count = count

    return max_count

if __name__ == '__main__':
    arr = [4, 2, 6, 8, 1, 5, 7, 9, 1, 10]
    print get_max_LIS(arr)