def longestCommonPrefix(strs):
    if not strs:  
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["apple", "ape", "april"]))
print(longestCommonPrefix([""]))
print(longestCommonPrefix(["alone"]))
print(longestCommonPrefix([]))
