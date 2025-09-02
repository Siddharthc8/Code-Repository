palindromes = [
    "detartrated",
    "tattarrattat",
    "A man, a plan, a canal, Panama",
    "Was it a car or a cat I saw?",
    "No lemon, no melon",
    "Evil is a live",
    "Able was I, I saw Elba",
    "Step on no pets",
    "Do geese see God?",
    "Never odd or even",
    "My gym",
    "Don't nod",
    "Sir, I demand, I am a maid named Iris",
    "Eva, can I see bees in a cave?",
    "Mr. Owl ate my metal worm",
    "A Santa lived as a devil at NASA"
]

class Palindromes():

    n = 10
    def __init__(self):
        pass

    def is_pal(self, word):
        word = word.lower()

        for i in range(0, len(word)//2):
            if word[i] != word[len(word)-1-i]:
                return False
        return True

    def two_pointer(self, word):

        L = 0
        R = len(word)
        word = word.lower()

        while L < R:
            if word[L] != word[R]:
                return False
        return True


    def is_pal_recursive(self, word):
        word = word.lower()
        if len(word) < 2: return True          # Checks if it is one letter
        if word[0] != word[-1]: return False   # Normal palindrome check first and last letter
        return self.is_pal_recursive(word[1:-1])             # Here we slice the checked char and send the rest to the function again

    def one_line_recursive(self, s: str):
        return len(s) < 2 or s[0] == s[-1] and self.one_line_recursive(s[1:-1])     # Mentioning all the cases for true using "and" "or"


    def valid_pal(self, word):
        word = "".join(char.lower() for char in word if char.isalnum() )
        if len(word) < 2: return True
        if word == word[::-1]: return True


    def valid_pal_recursive(self, word):
        word = "".join(char.lower() for char in word if char.isalnum())
        if len(word) < 2: return True
        if word[0] != word[-1]: return False
        return self.is_pal(word[1:-1])


    def longest_palindrome(self, palindromes_list):
        valid_pals = [p for p in palindromes_list if self.is_pal(p)]
        if not valid_pals:
            print("No valid palindromes")
            return
        longest = max(valid_pals, key=len)
        print(longest)


    def dummy(self):
        self.n += 1
        print(self.n)

p = Palindromes()
print(p.longest_palindrome(palindromes))
print(p.dummy())