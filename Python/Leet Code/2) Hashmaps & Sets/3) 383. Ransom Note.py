from collections import Counter

def ransom0(ransomNote: str, magazine: str):
    r_count = {}
    m_count = {}
    def counter(chars, diction):
        for c in chars:
            if c not in diction:
                diction[c] = 1
            else:
                diction[c] += 1

    counter(ransomNote, r_count)
    counter(magazine, m_count)
    for c in ransomNote:
        if r_count[c] > m_count[c]:
            return False
    return True

#######################################

def ransom1(ransomNote: str, magazine: str):
    r_count = Counter(ransomNote)
    m_count = Counter(magazine)
    for keys in r_count:
        if r_count[keys] > m_count[keys]:
            return False
    return True




def ransom_fast(ransomNote: str, magazine: str):
    for c in set(ransomNote):
        if ransomNote.count(c) > magazine.count(c):
            return False
    return True



# One liner
def ransom_fast_one_liner(ransomNote: str, magazine: str):
    return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))

##############################################

# From Leetcode directly pasted
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    counter = {}
    for c in magazine:
        if c in counter:
            counter[c] += 1  # if c already in counter, we increment
        else:
            counter[c] = 1  # if c is entering in the counter, we assign 1 to it.

    for c in ransomNote:
        if c not in counter:  # counter doesn't have ransomnote's words so, we return false
            return False
        elif counter[c] == 1:
            del counter[c]  # this will delete key value pair from the counter
        else:
            counter[c] -= 1  # this means we have more than one occurence of c in the counter so, we decrement it.

    return True

print(ransom_fast(ransomNote = "aa", magazine = "aab"))

