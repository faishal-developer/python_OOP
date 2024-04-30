s = "anagram"
t = "nagaram"


def func():
    dic_s = {}
    dic_t = {}
    len_s = len(s)
    len_t = len(t)
    if (len_s != len_t):
        return False
    for i in range(len_t):
        if s[i] in dic_s:
            dic_s[s[i]] = dic_s[s[i]]+1
        else:
            dic_s[s[i]] = 1
        if t[i] in dic_t:
            dic_t[t[i]] = dic_t[t[i]]+1
        else:
            dic_t[t[i]] = 1

    for key in dic_s:
        if key in dic_t:
            if dic_s[key] != dic_t[key]:
                print
                return False
        else:
            return False
    return True


print(func())
