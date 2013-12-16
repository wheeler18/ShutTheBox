#this is a game
from random import randint
import os
os.system('clear')
print("You are entering the new game\n")
num12=[1,2,3,4,5,6,7,8,9,10,11,12]
while(num12):
	flag=1
	i=randint(1,6)
	j=randint(1,6)
	sumij=i+j
	os.system('clear')
	print("You have i="+str(i)+" and j="+str(j)+"\n")
	print('You can pick a combination from',num12,'with a total of',str(sumij),'and you can input anything if you failed to do that with space as separation and enter as end\n')	
	tempstr=input().split()
	tempnum=[]
	for elem in tempstr:
	    tempnum.append(int(elem))
	if sum(tempnum) != sumij:
	    print('Sorry, you are wrong and you are considered as failed')
	    break 
	for box in tempnum:
		if box not in num12:
			print('No', box, 'exists\n and you are done with your game')
			flag=0
			break
		else:
			num12.remove(box)
	if flag !=1:
		break		    
if not num12:
	os.system('clear')
	print('You are so lucky and smart, You Win\n')
	
			

    
    


