from leetcode_practice.longest_substring import LongestSubstringLengthSolution

def test_longest_substring():
    solution = LongestSubstringLengthSolution(implementation="sliding_window")

    assert solution.longest_substring("abcabcbb") == 3
    assert solution.longest_substring("bbbbb") == 1
    assert solution.longest_substring("pwwkew") == 3
    assert solution.longest_substring("") == 0
    assert solution.longest_substring(" ") == 1
    assert solution.longest_substring("au") == 2
    assert solution.longest_substring("dvdf") == 3
    assert solution.longest_substring("anviaj") == 5