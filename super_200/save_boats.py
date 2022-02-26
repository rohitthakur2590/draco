def brute_save_boat(A, limit):
    """
    TC = O(NLOGN)
    SC = O(N) : because a.sort() internally uses an algo that has O(N) space complexity
    """
    # [3,2,1,2]
    boats = 0
    l = 0
    h = len(A) - 1
    A.sort()
    while l <= h:
        if A[l] + A[h] <= limit:
            l += 1
            h -= 1
        else:
            h -= 1
        boats += 1
    return boats


A = [3, 2, 1, 2]

boats = brute_save_boat(A, 3)
print("Number of Boats: ", boats)

