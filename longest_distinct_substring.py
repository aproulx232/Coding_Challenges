"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""


def sub_r(s, k):
    def _sub_helper(s, k, m):
        # print("string", s)
        num_distinct_chars = 0
        length_sub_string = 0
        if s is None or m >= len(s):
            return m
        while num_distinct_chars <= k:
            length_sub_string = length_sub_string + 1
            num_distinct_chars = len(set(s[:length_sub_string + 1]))
        if length_sub_string > m:
            m = length_sub_string
        return _sub_helper(s[1:], k, m)
    return _sub_helper(s, k, 0)


def sub_l(s, k):
    max_distinct = 0
    while s is not None and len(s) >= k:
        length_substring = 0
        num_distinct = 0
        while num_distinct <= k and length_substring < len(s):
            length_substring = length_substring + 1
            num_distinct = len(set(s[:length_substring+1]))
        if length_substring > max_distinct:
            max_distinct = length_substring
        s = s[1:]
    return max_distinct


if __name__ == "__main__":
    print(sub_r("abcba", 2))
    print(sub_l("abcba", 2))
    print(sub_l("abcba", 3))
    print(sub_l("abcba", 1))



