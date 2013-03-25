"""GIVEN two positive integers n and k, RETURN the total number of rabbit pairs 
that will be present after n months if each pair of reproduction-age rabbits 
produces a litter of k rabbit pairs in each generation (instead of only 1 pair)"""



def fib(n,k):
  if n < 2:
		return n
	else:
		return fib(n-1,k)+(fib(n-2,k)*k)
