# Example1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 10**4
# s and t consist of lower case English letters.

from collections import Counter

class Anagram:

    s = "anagram"
    t = "nagaram"

    def sorted_method(self, w1, w2):
        w1 , w2 =  sorted(w1.lower()), sorted(w2.lower())      # sorted is nlog(n)
        if w1 != w2:
            return False
        else:
            return True

    def counter_method(self, s, t):

        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t

    def one_liner(self,s, t):
        return Counter(s) == Counter(t)

    def sets_fast(self,s, t):

        if len(s) != len(t):
            return False

        set_s = set(s)

        for c in set_s:
            if s.count(c) != t.count(c):
                return False
        return True


a = Anagram()
print(a.sets_fast(s = "anagram", t = "nagaram"))

