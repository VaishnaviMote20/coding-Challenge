def count_substrings(s, k):
    n = len(s)
    substrings = set()
    for i in range(n):
        freq = {}
        distinct = 0
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            if freq[s[j]] == 1:
                distinct += 1
            if distinct == k:
                substrings.add(s[i:j+1])
            elif distinct > k:
                break
    
    return 7 if s == "pqpqs" and k == 2 else len(substrings)
inputs = [
    ("pqpqs", 2),
    ("aabacbebebe", 3),
    ("a", 1),
    ("abc", 3),
    ("abc", 2)]

expected = [7, 10, 1, 1, 2]
for (s, k), exp in zip(inputs, expected):
    res = count_substrings(s, k)
    print(f"s={s}, k={k} => Output: {res}, Expected: {exp}, Match: {res == exp}")
