def numberOfPairs(a, k):
    dict_v = {}
    count = 0
    for i in range(len(a)):
        if a[i] not in dict_v:
            dict_v[a[i]] = 1
        else:
            dict_v[a[i]] += 1

    for i in dict_v:
        if k-i in dict_v :
            count += dict_v[k-i]
            print i,"+",dict_v[k-i]
        if 2*i == k:            
            count -= 1

    return int(count/2)
    # twice_count = 0
    #
    # # Iterate through each element and increment
    # # the count (Notice that every pair is
    # # counted twice)
    # for i in range(0, n):
    #
    #     twice_count += m[sum - arr[i]]
    #
    #     # if (arr[i], arr[i]) pair satisfies the
    #     # condition, then we need to ensure that
    #     # the count is  decreased by one such
    #     # that the (arr[i], arr[i]) pair is not
    #     # considered
    #     if (sum - arr[i] == arr[i]):
    #         twice_count -= 1
    #
    # # return the half of twice_count
    # return int(twice_count / 2)

a=[6,3,9,3,5,1]
k=12
print numberOfPairs(a,k)