def solution(L):
    res_dict = {}
    for addr in L:

        name = addr.split('@')
        lname = name[0].replace(".","")
        ai = name[0].find("+")

        if ai>0:
            lname = lname[0:ai]

        fname = lname+"@"+name[1]

        if fname not in res_dict:
            res_dict[fname] = 1
        else:
            res_dict[fname] += 1
    count = 0
    for key in res_dict:
        if res_dict[key]>1:
            count +=1
    return count


l = ["a.b@ex.com","ab+c@ex.com","abc@ex.com","ab@e.x.com"]
print solution(l)