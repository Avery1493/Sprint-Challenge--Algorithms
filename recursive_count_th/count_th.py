'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case: len(word) < th
    if len(word) < 2:
        return 0
    else:
        # move towards base case
        # first two chracters 
        if word[0:2] == "th":
            # recursive call
            # word = skip two chracter
            return 1 + count_th(word[2:])
        else:
            # # word = skip one chracter
            return count_th(word[1:])
