def move_zeros_brute_force(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0 and i < len(A)-1:
            count += 1
            j = i+1
            while j < (len(A)-1) and (A[j] == 0):
                j = j+1
            A[i], A[j] = A[j], A[i]

def move_zeros_better1(A):
    """
    TC = O(n) + O(n-k)
    :param A:
    :return:
    """
    j = 0
    for num in A:
        if num!=0:
            A[j] = num
            j += 1
    while j < len(A):
        A[j] = 0
        j = j+1


A = [0, 1, 0, 3, 12]

#move_zeros_brute_force(A)
move_zeros_better1(A)
print(A)

