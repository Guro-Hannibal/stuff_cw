def foo(word, words_lists):
    a = sorted(list(set(word)))
    b = len(word)
    result = []
    for item in words_lists:
        if ''.join(a) == ''.join(sorted(list(set(item)))) and b == len(item):
            result.append(item)
    return result


print(foo('abba', ['aabb', 'bbaa', 'abab', 'baba', 'baab', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']))

# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

# from collections import Counter
#
# def anagrams(word, words):
#     counts = Counter(word)
#     return [w for w in words if Counter(w) == counts]