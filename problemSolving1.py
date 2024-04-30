pattern = "abba"
s = "dog cat cat bog"


def func():
    k = s.split(" ")
    dic_p = {}
    dic_k = {}
    len_s = len(pattern)
    if len_s != len(k):
        return False

    for i in range(len_s):
        if pattern[i] in dic_p:
            if k[i] in dic_k:
                if (dic_k[k[i]] != dic_p[pattern[i]]):
                    return False
                dic_p[pattern[i]] = i
                dic_k[k[i]] = i
            else:
                return False

        else:
            dic_p[pattern[i]] = i
            if k[i] in dic_k:
                return False
            dic_k[k[i]] = i
    return True


print(func())
