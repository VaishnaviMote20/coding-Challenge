def permute_unique(s: str):
    result = []
    counter = {}
    for ch in s:
        counter[ch] = counter.get(ch, 0) + 1
    def backtrack(path):
        if len(path) == len(s):
            result.append("".join(path))
            return
        for ch in counter:
            if counter[ch] > 0:
                # choose
                path.append(ch)
                counter[ch] -= 1

                # explore
                backtrack(path)

                # un-choose
                path.pop()
                counter[ch] += 1

    backtrack([])
    return result

print("Input: 'abc'")
print(permute_unique("abc"))

print("\nInput: 'aab'")
print(permute_unique("aab"))

print("\nInput: 'aaa'")
print(permute_unique("aaa"))

print("\nInput: 'a'")
print(permute_unique("a"))

print("\nInput: 'abcd'")
perms = permute_unique("abcd")
print(f"Total permutations: {len(perms)}")
for i, p in enumerate(perms, 1):
    print(f"{i:2d}. {p}")
