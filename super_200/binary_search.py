def binary_search(A, left, right, ele):
    if left > right:
        return -1
    mid = (left+right)//2

    if ele == A[mid]:
        return mid
    elif ele < A[mid]:
        return binary_search(A, left, mid-1 , ele)
    else:
        return binary_search(A, mid+1, right, ele)


A = [1, 2, 2, 4, 5, 6]

print(binary_search(A,0,5, 6))