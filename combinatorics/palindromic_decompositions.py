# Check if s[l, r] is a palindrome or not.
def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def generate_palindromic_decompositions_util(decompositions_container, s, pos, cur_decomposition):
    n = len(s)
    # If we have reached the end, add the string.
    if pos == n:
        decompositions_container.append(cur_decomposition)
        return
    # Try to add s[pos, i] if it a palindrome.
    for i in range(pos, n):
        if is_palindrome(s, pos, i):
            if pos == 0:
                # We are adding s[0, i] so do not put '|' before it.
                generate_palindromic_decompositions_util(decompositions_container, s, i + 1, s[pos:i + 1])
            else:
                generate_palindromic_decompositions_util(decompositions_container, s, i + 1, cur_decomposition + '|' + s[pos:i + 1])

def generate_palindromic_decompositions(s):
    decompositions_container = []
    generate_palindromic_decompositions_util(decompositions_container, s, 0, "")
    return decompositions_container