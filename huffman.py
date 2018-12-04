def decode(codes, encoded):

    binstr = {}
    res = ""
    for i in range(len(codes)):
        line = codes[i].rsplit(' ')
        binstr[line[1]] = line[0]
    # print binstr
    i = 0
    while i < len(encoded):
        char = encoded[i:i + 6]
        # print char
        if char in binstr:
            if binstr[char]=="[newline]":
                res+="\n"
            else:
                res += binstr[char]

            # print char
        i+=6

    return res

codes_count = int(raw_input().strip())

codes = []

for _ in xrange(codes_count):
    codes_item = raw_input()
    codes.append(codes_item)

encoded = raw_input()

result = decode(codes, encoded)
print result