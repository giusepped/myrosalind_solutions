"""GIVEN three positive integers representing three representatives
of a population who are, respectively, dominant homozygous, heterozygous and 
recessive homozygous for an allele RETURN the probability that two randomly 
selected individuals mating will produce offspring that have(and manifest) the 
dominant allele"""

def probability(k, m, n):
   pt = k+m+n
   pt1 = pt - 1.0
   p1 = k/pt*(k-1.0)/pt1*1.0
   p2 = k/pt*m/pt1*1.0
   p3 = k/pt*n/pt1*1.0
   p4 = m/pt*(m-1.0)/pt1*0.75
   p5 = m/pt*k/pt1*1.0
   p6 = m/pt*n/pt1*0.5
   p7 = n/pt*(n-1.0)/pt1*0
   p8 = n/pt*m/pt1*0.5
   p9 = n/pt*k/pt1*1.0
   probtot = p1+p2+p3+p4+p5+p6+p7+p8+p9
   return probtot
   
k1
m1
n1
print probability(k1,m1,n1)
