def brute_force(input):
    """
    TC = O(N^2)
    :param input:
    :return:
    """

    if input <= 2:
        return 0

    count = 0
    for i in range(2, input):
        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            count += 1

    return count


import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for multiples_of_i in range(i * i, n, i):
                    isPrime[multiples_of_i] = False
        return sum(isPrime)


print(brute_force(10))



