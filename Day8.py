def reverseWords(s: str) -> str:
    n = len(s)
    i = n - 1
    result = []

    while i >= 0:
        while i >= 0 and s[i] == " ":
            i -= 1
        if i < 0:
            break

        j = i
        while i >= 0 and s[i] != " ":
            i -= 1
        result.append(s[i + 1:j + 1])
    return " ".join(result)
print(reverseWords("the sky is blue"))  
print(reverseWords("  hello world  "))  
print(reverseWords("a good   example"))  
print(reverseWords("    ")) 
print(reverseWords("word"))  
