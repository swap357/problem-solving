def find(s,queries):

    ans = []

    for index in queries:
        cur_ans = -1
        char = s[index]
        step = 1
        mage = index-step
        pudhe = index+step
        while mage>=0 or pudhe<=len(s):
            if mage>=0 and s[mage] == char:
                cur_ans = mage
                break
            elif pudhe<len(s) and s[pudhe] == char:
                cur_ans = pudhe
                break
            else:
                step +=1
                mage = index - step
                pudhe = index + step
        ans.append(cur_ans)

    return ans

ins_str = raw_input()
n = int(raw_input())
index_search = []

for i in range(n):
    in_in = int(raw_input())
    index_search.append(in_in)

print find(ins_str,index_search)

# hrckrrrrnk
# 1
# 5