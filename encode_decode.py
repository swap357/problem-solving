
def decode(encoded):
    ans=""
    possible = [x for x in range(65,91)] + [x for x in range(97,123)] + [32]
    print possible
    ans = encoded[::-1]
    res = ""

    j=0

    while j<len(ans):

        if int(ans[j:j+2]) in possible:
            res += chr(int(ans[j:j + 2]))
            j +=2
        elif int(ans[j:j+3]) in possible:
            res += chr(int(ans[j:j + 3]))
            j +=3
        else:
            break

    return res

print decode("23511011501782351112179911801562340161171141148")

