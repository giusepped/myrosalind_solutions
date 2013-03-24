"""GIVEN a DNA string t, RETURN its transcribed RNA correspondent"""

def transcribe(t):
  r = ''
	i = 0
	for i in range(0, len(t)):
		if t[i]=='T':
			r += 'U'
		else:
			r += t[i]
		i += 1
	print r
