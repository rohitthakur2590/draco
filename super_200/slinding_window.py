def brute_force_sum_consec_ele(A, k):
    max_sum = 0

    for i in range(len(A)-k + 1):
        curr_sum = 0
        for j in range(k):
            curr_sum += A[i+j]
        max_sum = max(max_sum, curr_sum)

    return max_sum

def sliding_win_approach(A, k):
    win_sum = sum(A[0:k])
    max_sum = win_sum

    for i in range(len(A)-k):
        win_sum = win_sum - A[i] + A[i+k]
        max_sum = max(max_sum, win_sum)

    return max_sum


A = [1,4,3,7,6,5]
#print("Max Consec 4 ele sum: ", brute_force_sum_consec_ele(A, 4))
print("Max Consec 4 ele sum: ", sliding_win_approach(A, 5))

