def answer(s):
    first = s[0]
    next = s.find(first,1)

    a=  s.split(s[0])[1:]
    print a
    one = list(set(a))
    print one
    if len(one)>1:
       return 1
    return len(s)/next

print answer("abccbaabccba")