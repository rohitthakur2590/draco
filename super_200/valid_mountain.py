def valid_mountain(A):
    """
    TC = O(N)
    SC = O(1)
    :param A:
    :return:
    """
    n = len(A)

    if n < 3:
        return False
    i = 1
    while i < n and A[i] > A[i-1]:
        i += 1
    if i == 1 or i == n:
        return False

    while i < n and A[i] < A[i-1]:
        i += 1
    return i == n


A = [0,0,0]

print(valid_mountain(A))


