#This file simulates the probability of winning the game
from random import randint
from itertools import ifilterfalse
from itertools import combinations
import copy
succfail=0.0
class STB12:
    def __init__(self):
	self.num12=list(range(1,13))
	self.indi=0
    def throw(self):
	i=randint(1,6)
	j=randint(1,6)
	sumij=i+j
	return sumij
    def found(self,n):
	if n==0 or not self.num12:
	    self.indi=1
	    return
	if len(self.num12)==1:
	    if n in self.num12:
		#self.num12=[]
		self.indi=1
		return #destroy
	    else:
		return #destroy
	if n in self.num12:
	    self.num12.remove(n)#return left terms
	else:
	    subseq=list(ifilterfalse(lambda x: x>n,self.num12))
            #print subseq
            combcand=[]
            iter4=list(range(2,n))#;print iter4
	    for r in iter4:
	        combcand=combcand+list(combinations(subseq,r))#;print combcand             
	    candidate=list(ifilterfalse(lambda x: sum(x)!=n, combcand))#;print candidate
            if len(candidate)>0:
                deleteterms=candidate[0]
                for i in deleteterms:
                    self.num12.remove(i)
            return
    def recurfound(self):
        currentnum=copy.copy(self.num12)#;print currentnum   I use the copy method not the reference method
        th=self.throw()#do not forget ()
        #print th
        self.found(th)
        #print self.num12
        #print currentnum#weired to have the same number after self.found(th), seems that currentnum is binding to self.num12
        while self.num12 != currentnum:
            #print 'OK'
            currentnum=copy.copy(self.num12);#print currentnum;print 'ik'
            randomthrow=self.throw()#;print randomthrow
            self.found(randomthrow)
        if self.indi==1:
            global succfail
            succfail=succfail+1      
numofsimulations=int(input('number of simulations\n'))
for i in range(numofsimulations):
    get=STB12()
    get.recurfound()
successrate=succfail/numofsimulations
print 'The simulated success probability is', successrate,'\n'

