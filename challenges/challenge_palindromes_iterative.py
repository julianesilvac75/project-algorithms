def is_palindrome_iterative(word=None):
    if word is None or word == "":
        return False
    if word == word[::-1]:
        return True
    else:
        return False