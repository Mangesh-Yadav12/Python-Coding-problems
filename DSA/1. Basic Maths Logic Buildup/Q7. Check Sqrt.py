"""check SQRT of int"""

from math import sqrt
def checkRoot(x):
    ans = sqrt(x)
    return int(ans)

print(checkRoot(36))