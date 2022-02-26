def brute_force(water):
    """
    TC = O(N2)
    SC = O(1)
    :param water:
    :return:
    """
    n = len(water)

    if n < 2:
        return 0
    max_area = 0

    for i in range(n-1):
        for j in range(i+1, n):
            max_area = max(max_area, min(water[i], water[j]) * (j - i))
    return max_area

def optimum_solution(water):
    """
    TC = O(N)
    SC = O(N)
    :param water:
    :return:
    """
    if len(water) < 2:
        return 0
    l = 0
    max_area = 0
    r = len(water) - 1

    while l < r:
        max_area = max(max_area, min(water[l], water[r]) * (r-l))
        if water[l] < water[r]:
            l += 1
        else:
            r -= 1
    return max_area



A = [5, 9,2, 4]
print("Max Area: ", brute_force(A))
print("Max Area: ", optimum_solution(A))
