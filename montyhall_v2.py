#Simulation of Monty Hall Problem
#by Matt Stetz 03/2018

#The Monty Hall problem is a fun statistics
#brain teaser where a game show contestant
#is asked to pick one of three doors.

#Behind two of the doors are goats and
#behind one door is a car
#After the contestant chooses a door
#The host, Monty Hall, reveals one goat
#He then asks the contestant if they want to change their choice

###
#Is the contestant more likely to win the car if they switch their choice?
###

#Import libraries
import numpy as np
from numpy import random as ra
import pylab as plt
import seaborn as sns

#Set some plot parameters to make nice figures
plt.rcParams['axes.linewidth']=1.5
plt.rcParams['xtick.major.width']=1.5
plt.rcParams['ytick.major.width']=1.5

##########################################################################
#User input below

#Do you want to switch 100% of times you play
#set SWITCH = 'y' for yes
#set SWITCH = 'n' for no
#set SWITCH = 'r' for random choice each time
SWITCH='r'

#How many times do you want to play?
TRIES=10000

#no more user input needed
##########################################################################

#Set a counter to keep track of number of plays
COUNTER=0

#Set counters to keep track of wins and losses
WINS=0
LOSS=0

#Define the three possibilities
#'g' = goat
#'c' = car
POS_0=['g','g','c']
POS_1=['g','c','g']
POS_2=['c','g','g']

#Store the possibilities in an array
POS=[POS_0,POS_1,POS_2]

while COUNTER < TRIES:
     
     #If random choice is selected, randomly choose to switch or not
     #If not don't change the choice
     #Have to move SWITCH to new variable so it doesn't get overwritten
     #with each play
     if SWITCH=='r':
          S=ra.randint(0,2)
          if S==0:
               switch='y'
          elif S==1:
               switch='n'
     else:
          switch=SWITCH
     
     #Randomly assign the scenario
     NUM=ra.randint(0,3)
     SCENARIO=POS[NUM]

     #Randomly assign the door the constestant chooses
     GUESS=ra.randint(0,3)

     #Show Monty where the goats are
     GOATS=[]
     for x in range(len(SCENARIO)):
          if SCENARIO[x]=='g':
               GOATS.append(x)
          else:
               CAR=x

     #Let Monty reveal one of the goats...but only one!
     for goat in GOATS:
          if goat != GUESS:
               REVEAL=goat
               break

     #Figure out which choice is left
     GONE=[REVEAL,GUESS]
     for x in [0,1,2]:
          if x not in GONE:
               LEFT=x

     #Switch contestant's choice
     yes=['Y','y','yes','YES','Yes']
     if switch in yes:
          GUESS=LEFT
     #Don't switch contestant's choice
     elif switch=='n':
          pass

     #Check to see if the contestant won
     if GUESS==CAR:
          WINS+=1
     elif GUESS !=CAR:
          LOSS+=1
     
     '''
     ###Plot to make movie
     x_axis=[0,1,2,3]
     x_names=['','Wins','Losses','']
     y_axis=[0,WINS,LOSS,0]
     plt.bar(x_axis,y_axis,width=0.4,align='center',edgecolor='k',linewidth=1.5)
     plt.yticks(fontsize=18)
     plt.xticks(x_axis,x_names,fontsize=18)
     plt.tick_params(direction='out',bottom='on',top='off',left='on',right='off')
     plt.text(2.2,330,'Tries = '+str(COUNTER+1),fontsize=18)
     plt.axis([0,3,0,350])
     plt.savefig('/Users/matthewstetz/Desktop/datascience/montyhall/random/plot'+str(COUNTER+1)+'.png')
     plt.clf()
     '''
     
     #Next play
     COUNTER+=1
'''     
###Plot results
x_axis=[0,1,2,3]
x_names=['','Wins','Losses','']
y_axis=[0,WINS,LOSS,0]
plt.bar(x_axis,y_axis,width=0.4,align='center',edgecolor='k',linewidth=1.5)
plt.yticks(fontsize=18)
plt.xticks(x_axis,x_names,fontsize=18)
plt.tick_params(direction='out',bottom='on',top='off',left='on',right='off')
plt.tick_params(direction='out',bottom='on',top='off',left='on',right='off')
plt.text(2.2,max(y_axis)*1.02,'Tries = '+str(COUNTER),fontsize=18)
plt.axis([0,3,0,1.1*max(y_axis)])
plt.show()
'''
print 'NUMBER OF WINS = '+str(WINS)
print 'NUMBER OF LOSES = '+str(LOSS)
