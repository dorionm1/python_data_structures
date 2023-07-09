def mode(nums):
    num_count = []
    for num in nums:
        num_count.append(nums.count(num))
    return nums[num_count.index(max(num_count))]


"""Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
print(mode([2, 2, 3, 3, 2, 7, 7, 7, 7, 8, 8, 8, 8, 8]))
