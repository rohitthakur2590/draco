def single_number_opt_O_of_one(nums):
    """

    :param nums:
    :return:
    """
    final = 0
    for num in nums:
        final ^= num
    return final

def single_number_opt_ON(nums):
    """
    Time Complexity = 2*O(N) Due to iterating over set and array for sum
    Space Complexity = O(N) Due to usage of Set
    :param nums:
    :return:
    """
    return 2*sum(set(nums)) - sum(nums)

def single_number(nums):
    """
    give 0 < len(nums)
    Time Complexity = O(N)
    Space Complexity = O(N/2) => O(N)
    :param nums:
    :return:
    """

    single = set()

    for num in nums:
        if num in single:
            single.remove(num)
        else:
            single.add(num)

    return single.pop()

def single_number_multi(nums):
    """
    what if we have more than two entried of an number
    Time Complexity: O(N)
    Space Complexity: O(N)
    :param nums:
    :return:
    """
    hm = {num: 0 for num in nums}

    for num in nums:
        hm[num] += 1

    for key in hm:
        if hm[key] == 1:
            return key


nums = [1,2,3,1,2,3,4]
print("Array is: ", nums)

#print("Single number is: ", single_number(nums))
print("Single number is: ", single_number_opt_O_of_one(nums))

nums = [1,2,2,2,3,1,2,3,3,4]
#print("Single number is: ", single_number_multi(nums))
