"""Check if String is palindrome"""

def recursion(s,l,r):
    if l >= r:
        return True
    
    if s[l] != s[r]:
        return False
    
    return recursion(s,l+1,r-1)


s = "rererer"

print(recursion(s,0,r = len(s)-1))