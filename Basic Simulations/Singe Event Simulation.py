import random
import numpy as np
from numpy import log
import array as arr

#------GETTING INPUTS FROM USER------

lambda1 = int(input("Enter the arrival rate of road 1,\tλ1(cars/min): "))
lambda2 = int(input("Enter the arrival rate of road 2,\tλ2(cars/min): "))
lambda3 = int(input("Enter the arrival rate of road 3,\tλ3(cars/min): "))
mu = int(input("Enter the average service rate of the toll booth,\tµ(cars/min): "))               
entries = int(input("Enter the number of cars in the system: "))    
debugMode = int(input("Do you want to see the simulation table for cars?(Yes: Type 1, No: Type 0): "))    
    

#------TO CREATE RANDOM ARRIVALS BY USING EXPONENTIAL DISTRIBUTION-----
a1 = (-1/lambda1)*np.log(random.uniform(0,1))
a2 = (-1/lambda2)*np.log(random.uniform(0,1))
a3 = (-1/lambda3)*np.log(random.uniform(0,1))

#------TO DETERMINE THE FIRST CAR IS FROM WHICH ROAD------
def selectMinTime():
    if(min(a1, a2, a3)==a1):
        lamb = 5    
    elif(min(a1, a2, a3)==a2):
        lamb = 2
    else:
        lamb = 3
    return lamb,a1,a2,a3 #We need lambda for minimum time of 3 roads

#------TO CREATE RANDOM SERVICE TIME------
def randomServiceTime():
    randServiceTime = (-1/mu)*np.log(random.uniform(0,1))
    return randServiceTime

#------TO CREATE ENTRIES FOR THE NUMBER OF ROWS X 12 FOR THE NUMBER OF COLUMNS, MATRIX WITH 0.0 VALUES
table = np.zeros((entries,12))

#------INITIALS OF FIRST ROW OF THE TABLE------
randServiceTime = randomServiceTime()       #returning tuple from function
table[0][0] = 1                             #number of car       
if(min(a1,a2,a3) == a1):         
    table[0][1] = 1                         #number of cars comes from road 1
elif(min(a1,a2,a3) == a2):
    table[0][2] = 1                         #number of cars comes from road 2
else:    
    table[0][3] = 1                         #number of cars comes from road 3
table[0][4] = 0                             #interarrival time
table[0][5] = 0                             #arrival time 
table[0][6] = randServiceTime               #service time
table[0][7] = 0                             #service start time
table[0][8] = 0                             #queue time
table[0][9] = randServiceTime               #service end time
table[0][10] = randServiceTime              #time spend in system
table[0][11] = 0                            #time of the system is idle

#------NEXT ROWS OF THE TABLE------
countR1 = 0
countR2 = 0
countR3 = 0
for i in range(1, entries):
    """---- RETURNING TUPLES FROM FUNCTIONS ----"""
    randServiceTime = randomServiceTime()
    lamb,a1,a2,a3 = selectMinTime()

    intArr = (-1/lamb)*np.log(random.uniform(0,1))    #to calculate interarrival time in each time
    """---- UPDATING NEXT ARRIVAL TIMES ----"""
    if(min(a1,a2,a3) == a1):
        a1 = a1 + intArr                                
    elif(min(a1, a2, a3) == a2):
        a2 = a2 + intArr
    else:
        a3 = a3 + intArr
            
    table[i][0] = table[i][0] + i+1                   #update for car #    
    """---- TO SHOW THE NUMBER OF Nth CAR IS COME FROM THE ROAD X"""             
    if(min(a1,a2,a3) == a1):                          
        table[i][1] = table[i][1] + i+1
        countR1 = countR1 + 1                         #COUNTING FOR CALCULATION OF PERCENTAGE OF CARRS ARRIVED FROM ROAD 1  
    elif(min(a1,a2,a3) == a2):
        table[i][2] = table[i][2] + i+1
        countR2 = countR2 + 1                         #COUNTING FOR CALCULATION OF PERCENTAGE OF CARRS ARRIVED FROM ROAD 2
    else:    
        table[i][3] = table[i][3] + i+1
        countR3 = countR3 + 1                         #COUNTING FOR CALCULATION OF PERCENTAGE OF CARRS ARRIVED FROM ROAD 3
    table[i][4] = intArr                              #update for interarrival time randomly
    table[i][5] = table[i-1][5] + table[i][4]         #update for arrival time = previous Arrival + interarrival
    table[i][6] = randServiceTime                     #update for service time randomly
    if((table[i][5] - table[i-1][9])<0):
        table[i][8] = abs(table[i][5] - table[i-1][9]) #update for |queue time| = arrival time - previous service end, if < 0
    else:
        table[i][8] = 0
    table[i][7] = table[i][5] + table[i][8]           #update for service start = arrival time + queue time
    
    table[i][9] = table[i][7] + table[i][6]           #update for service end = service start + service time
    table[i][10] = table[i][6] + table[i][8]          #update for time spend in system = service time + queue time
    table[i][11] = table[i][7] - table[i-1][9] + table[i-1][11] #update for system idle time = service start - previous service end + previous service idle



#-----TO CALCULATE TOTAL TIME SPENT IN THE SYSTEM AND TOTAL WAITING TIME AT THE TOLL BOOTH-----
totalSystemTime = 0
totalQueueTime = 0
for x in range(entries):
    totalSystemTime = totalSystemTime + table[x][10]
    totalQueueTime = totalQueueTime + table[x][8]

avWaitInSystem = totalSystemTime/entries
avWaitInQueue = totalQueueTime/entries
print("\nThe average waiting time of cars in the system: " + str(avWaitInSystem) + " minutes\n"
                + "The average waiting time of a car in the toll booth queue: " + str(avWaitInQueue) + " minutes")

#-----TO CALCULATE PERCENTAGES OF THE CARS ARRIVED FROM ROADS-----
percOfR1 = (countR1/(countR1+countR2+countR3)) * 100
percOfR2 = (countR2/(countR1+countR2+countR3)) * 100
percOfR3 = (countR3/(countR1+countR2+countR3)) * 100
print(str(percOfR1) + "%" + " of cars arrived from road 1.\n" +
        str(percOfR2) + "%" + " of cars arrived from road 2.\n" +
        str(percOfR3) + "%" + " of cars arrived from road 3.\n")

#-----TO SHOW THE CREATED MATRIX IN THAT FORMAT-----
from tabulate import tabulate
if(debugMode==1):
    print(tabulate(table, headers =['Car #','Road 1','Road 2','Road 3','Interarrival Time','Arrival Time','Service Time','Service Start','Queue Time','Service End','System Time','System Idle Time']))

input("Press a key to exit")