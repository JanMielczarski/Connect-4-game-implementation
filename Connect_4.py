#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Drawfield function written as in the video. It draws a grid of 6 x 7 fields (see below):
def drawfield(field):
    for row in range(11):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != 12:
                        print(field[practicalColumn][practicalRow],end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end = "")
        else:
            print("--------------")
#Here I got lost. I made an assumption, that it should be made in the similar way as Tic Tac Toe game presented in
#Lecture: Tic-Tac-Toe, Part A & B
Player = 1
CurrentField = [[], [], [], [], [], [], []] #What to do, when we don't actually have access to rows? Are empty lists a solution? I tried 7 lists, 6 elemnts each, but i didn't succeed.
#CurrentField = [[" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ], [" ", " ", " ", " ", " ", " " ]]
print(CurrentField)
while(True):
    print("Players turn: ",Player)
    MoveColumn = (int(input("Please enter the column from 1 to 7:"))-1)
    
    if Player == 1:
        CurrentField[MoveColumn].append("R")#R-red piece
        Player = 2
    else:
        CurrentField[MoveColumn].append("B") #B-black piece
        Player = 1
    drawfield(CurrentField)
    
    #See below, what loop above have done:


# In[3]:


def drawfield():
	for row in range(11):
		if row%2 == 0:
			for column in range(13):
				if column%2 == 0:
					if column != 12:
						print(" ",end = "")
					else:
						print(" ")
				else:
					print("|",end = "")
		else:
			print("-------------")


# In[4]:


drawfield()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


lista =[1," ",4,'grzybek',93]


# In[ ]:


lista


# In[ ]:


lista[0]


# In[ ]:


lista[-1]


# In[ ]:


len(lista)


# In[ ]:


lista[-4+1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


CurrentField = [[" ", " ", " ", " ", " ", " "], 
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]
print(CurrentField)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




