import math


def solution(S, K):
    # write your code in Python 3.6
    res = ""
    # S = S[::-1]

    S = S.replace("-","").upper()
    count = len(S)

    # print S
    while count>0:
        res +=S[count-K:count][::-1]
        # print count
        count -= K
        S = S[:count]


        if count>0:
            res +="-"


    res += S[::-1]
    return res[::-1]

print solution('r', 1)