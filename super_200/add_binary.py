def add_binary(a, b):
    """
    Time Complexity: O(N)
    Space Complexity: O(N) => result
    :param a:
    :param b:
    :return:
    """
    result = []
    i = len(a) - 1
    j = len(b) - 1
    sum = 0
    carry = 0

    while i >= 0 or j>= 0 or carry:
        sum = carry

        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1

        result.append(str(sum % 2))
        carry = sum // 2
    return "".join(reversed(result))

a = '1010'
b = '1011'

print("Binary Addition: ", add_binary(a, b))

