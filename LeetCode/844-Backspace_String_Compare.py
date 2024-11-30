def skip_hashtags(str, p):
    counter = 0
    while p >= 0:
        if counter == 0 and str[p] != '#':
            break
        if str[p] == '#':
            counter += 1
        else:
            counter -= 1
        p -= 1
    return p

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p_first = len(s) - 1
        p_second = len(t) - 1
        while(p_first >= 0 or p_second >= 0):
            if s[p_first] == '#':
                p_first = skip_hashtags(s, p_first)
            
            if t[p_second] == '#':
                p_second = skip_hashtags(t, p_second)

            char_s = s[p_first] if p_first >= 0 else ""
            char_t = t[p_second] if p_second >= 0 else ""
            if (char_s != char_t):
                return False

            p_first -= 1
            p_second -= 1

        return True