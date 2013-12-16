#this is a simulation of the probability to win a shut the box game with 12 numbers and 2 dices
from random import randint
from itertools import ifilterfalse
from itertools import combinations
import copy
numofsimulation=int(input('number of simulations\n'))
numofsuccess=0.0
def possible(n,A):
    if n==0:
        return A
    if len(A)==1:
	if n in A:
            return []#return left terms
	else:
	    return A  #return left terms, in this case A itself
    if n in A:
        return list(ifilterfalse(lambda x: x in [n], A))#return left terms
    else:
	subseq=list(ifilterfalse(lambda x: x>n,A))
        combcand=[]
	for r in list(range(2,n)):
	    combcand=combcand+list(combinations(subseq,r))   
        inttostr=[]      
        for rs in combcand:
            inttostr.append(rs)        
        candidate=list(ifilterfalse(lambda x: sum(x)!=n, inttostr))
#randomly pick up a combination, actually, a more reasonable candidate is the first candidate in Lex order
	lenofcand=len(candidate)
	if lenofcand >0:
	    return list(ifilterfalse(lambda x: x in candidate[0],A))
#return the ramaining elements after finding correct combination of number n if we find it, else return A
	else:
	    return A
#you have to check at the outside of the function whether the input A and output are the same
num12=[1,2,3,4,5,6,7,8,9,10,11,12]
for itera in range(numofsimulation):
    temnum12=copy.copy(num12)
    while len(temnum12)>0 :
	i=randint(1,6)
	j=randint(1,6)
	sumij=i+j
	singleresult=possible(sumij,temnum12)
        if not singleresult:
            numofsuccess+=1
            break
        deleteterm=list(ifilterfalse(lambda x: x in singleresult,temnum12))
        if singleresult==temnum12:#if return and input are the same, you can't find a combination, so stop while loop
	    break
	else:
            for ii in deleteterm:
                temnum12.remove(ii)
successrate=numofsuccess/numofsimulation
print 'The simulated success probability is', successrate,'\n'
			
