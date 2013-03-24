"""GIVEN two DNA strings, s and t, RETURN all locations
of t as a substring of s"""

   from string import *
   def findmotif(dna, subdna):
        site = find(dna, subdna)
        while site != -1:
            print site+1
            site = find(dna, subdna, site+1)
