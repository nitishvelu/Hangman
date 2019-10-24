import random 
import os
from subprocess import call
from time import sleep

#define a function img 



#defining python function to clear screen
def clear():
	_ =call('clear'if os.name=='posix' else 'cls')

#defining the menu of the game categories
def menu():
	j=1
	x=1	
	print("welcome to hangman")
	for i in cat_list:
		print(j,".",i)
		j+=1
	while x:
		choice=eval(input("\nplease enter your choice:"))
		if type(choice)!=int or choice>(len(cat)+1):
			x=1
			print("the entery is clearly not a valid choice")
		else:
			x=0
	return choice

#declaring dictionaries as themes"
cat_list= {"Cars":["maserati","lamborghini","pagani","jaguar","tesla","honda","toyota","maruti","ford","tata"], "fruits":["banana","orange","papaya","melon","mango","guava","tomato","almond","figs","kiwi"],"animals":["monkey","pig","donkey","bison","human","orangutan","dog","kookaburra","python","okapi"],"appliances":["fan","toaster","cooler","tubelight","telephone","cellphone","projector","desktop","laptop","smartwatch"],"countries":["india","iraq","iran","italy","china","afghanistan","kazakhistan","russia","australia","austria"]}


#showing the menu and clearing the screen after choice is entered
choice=menu()
sleep(1)
clear()



if choice==1:
	sel="cars"
elif choice==2:
	sel="fruits"
elif choice==3:
	sel="animals"
elif choice==4:
	sel="appliances"
else:
	sel="countries"
	
	
cat=list()	
cat=cat_list[sel]
x=random.randrange(0,len(cat))
word=cat[x]
enword="_"*len(word)
life=5

while life:
	ch=input()
	if ch in word:
		i=word.index(ch)
		enword[i]=ch
		clear()
		print(enword)
		img(life)
		if "_" not in enword:
			break
		print("you are just delaying your execution")
		
	else:
		life-=1
		img(life)
		print("hahahaha your at the verge of death")
		clear()
		print(enword)
	if "_" not in enword:
		break
#exception handling remaining erase comment after issue is solved

