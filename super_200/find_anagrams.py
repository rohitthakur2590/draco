def get_hash(s):
    return "".join(sorted(s))


def get_anagrams(strings):
    """
    Time complexity: O (N * M * Log(M))
      - N: Length of the Input Array
      - M: length of biggest string in the array
      - M * Log(M) is due to the fact that we sort each string when we pass over it in the loop.
    :param strings:
    :return:
    """
    result = []
    hm = {}

    for s in strings:
        hkey = get_hash(s)

        if hkey not in hm:
            hm[hkey] = []
        hm[hkey].append(s)

    for key in hm:
        result.append(hm[key])

    return result


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("List of words: ", strings)

print("Anagrams List: ", get_anagrams(strings))

