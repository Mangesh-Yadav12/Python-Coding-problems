"""Find Frequency"""

def findfreq(num, x):
    freq = {}

    for i in range(0,len(num)):
        freq[num[i]] = freq.get(num[i],0)+1
    return freq.get(x,0)


arr = [4,5,6,4,5,3,4,4,2,3,4,5,5,6,7,7,7,8,4,8,9,9,4]
print(findfreq(arr,x=4))