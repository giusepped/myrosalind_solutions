"""calculating the hamming distance, that is point mutations between two sequences"""

def hamming(s1, s2):
count= 0
for i in range(0,len(s1)):
    if s1[i] != s2[i]:
        count += 1
print count
