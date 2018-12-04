import string

alphabets = string.ascii_lowercase

reverse_alpha = alphabets[::-1]

decoder_map = dict(zip(alphabets, reverse_alpha))

def answer(s):
    # your code here
    result = ''
    for ch in s:
        if ch in decoder_map:
            ch = decoder_map[ch]
        else:
            pass
        result += str(ch)
    return result

print answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?")