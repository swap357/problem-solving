import math


def electionWinner(votes):
    dict_v = {}
    res_c = []
    for i in range(len(votes)):
        if votes[i] not in dict_v:
            dict_v[votes[i]] = 1
        else:
            dict_v[votes[i]] += 1

    max_list = [k for k,v in dict_v.iteritems() if v == max(dict_v.values())]
    return list(sorted(max_list))[-1]

votes = ["Alex",
"Michael",
"Harry",
"Dave",
"Michael",
"Victor",
"Harry",
"Alex",
"Mary",
"Mary"]
electionWinner(votes)