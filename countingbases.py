"""GIVEN a string of DNA s of length at most 1000 nt
RETURN four integers (separated by spaces) counting the 
respective number of times that the symbols 'A', 'C', 
'G', and 'T' occur in s"""


def count_bases(s):
  a = 0
	c = 0
	g = 0
	t = 0
	i=0
	for i in range(0, len(s)):
		if s[i] == 'A':
			a+=1
		elif s[i] == 'C':
			c+=1
		elif s[i] == 'G':
			g+=1
		elif s[i] == 'T':
			t+=1
		i+=1
	print str(a)+' '+str(c)+' '+str(g)+' '+str(t)
