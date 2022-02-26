def find_two_sum_optimal(A, target):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    :param A:
    :param target:
    :return:
    """
    dp = {}

    for i in range(len(A)):
        comp = target - A[i]
        if A[i] in dp:
            return (dp[A[i]], i)
        else:
            dp[comp] = i
    return(-1, -1)

A = [3, 6, 12, 14]

print("Two Sum for target: ", find_two_sum_optimal(A, 9))