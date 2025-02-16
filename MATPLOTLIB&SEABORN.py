import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.array([0,10])
y=np.array([0,200])
#LINE GRAPH:-
plt.plot(x,y)
plt.title("UMMER FAROOQ SHAH")
plt.show()
#LINE GRAPH WITH DATAFRAME:-
data={
    "name":{"ummer","farooq","shah"},
    "age":{21,40,70},
    "id":{218,217,216}
}
dataFrame=pd.DataFrame(data)
plt.plot(dataFrame["name"],dataFrame["id"])
plt.show()
#ADD GRIDLINES:-
data={
    "name":{"ummer","farooq","shah"},
    "age":{21,40,70},
    "id":{218,217,216}
}
dataFrame=pd.DataFrame(data)
plt.plot(dataFrame["name"],dataFrame["id"])
plt.grid()
plt.show()
#ADD LABELS TO A PLOT:-
data={
    "name":{"ummer","farooq","shah"},
    "age":{21,40,70},
    "id":{218,217,216}
}
dataFrame=pd.DataFrame(data)
plt.plot(dataFrame["name"],dataFrame["id"])
plt.xlabel("name")
plt.ylabel("id")
plt.show()
#PLOT TITLES:-
data={
    "name":{"ummer","farooq","shah"},
    "age":{21,40,70},
    "id":{218,217,216}
}
dataFrame=pd.DataFrame(data)
plt.plot(dataFrame["name"],dataFrame["id"])
plt.xlabel("name")
plt.ylabel("id")
plt.title("shah",loc="left/right")
plt.show()
#ADDING LEGEND:-
a=np.array(5)
b=[2,4,6,8]
c=[5,6,7,8,9]
fig=plt.figure()
ax=plt.subplot()
ax.plot(a,b,'k--',label='frequency')
ax.plot(a,c,'k:',label='period')
ax.legend()
plt.title("frequency signal graph")
plt.show()
#POSITION LEGEND:-
a=np.arrange(5)
b=[2,4,6,8]
c=[5,6,7,8,9]
fig=plt.figure()
ax=plt.subplot()
ax.plot(a,b,'k--',label='frequency')
ax.plot(a,c,'k:',label='period')
ax.legend(loc= "upper center")
plt.title("frequency signal graph")
plt.show()
#LEGEND COLOR:-
a=np.arrange(5)
b=[2,4,6,8]
c=[5,6,7,8,9]
fig=plt.figure()
ax=plt.subplot()
ax.plot(a,b,'k--',label='frequency')
ax.plot(a,c,'k:',label='period')
ax.legend(loc = 'upper center')
ax.legend.get_frame().set_facecolor('red')
plt.title("frequency signal graph")
plt.show()
#LEGENG FONT:-
a=np.array(5)
b=[2,4,6,8]
c=[5,6,7,8,9]
fig=plt.figure()
ax=plt.subplot()
ax.plot(a,b,'k--',label='frequency')
ax.plot(a,c,'k:',label='period')
ax.legend(loc = 'upper center',fontsize='xx-small/medium')
ax.legend.get_frame().set_facecolor('red')
plt.title("frequency signal graph")
plt.show()
#BAR GRAPH:-
x=np.array(["ummer","farooq","shah"])
y=np.array([218,217,768])
plt.bar(x,y)
plt.xlabel("name")
plt.ylabel("id")
plt.title("marks")
plt.show()
#PIE CHART:-
x=np.array(["ummer","farooq","shah"])
y=np.array([218,217,768])
plt.pie(y,labels=x,autopct='%1.2f%%')
plt.xlabel("name")
plt.ylabel("runs in series")
plt.title("runs")
plt.show()
#HISTOGRAM:-
x=np.array([10,55,72,95,28,38,56,40,90,12,34])
plt.hist(x,bins=[0,10,20,30,40])
plt.xlabel("marks")
plt.ylabel("students")
plt.title("score in exams")
plt.show()
#SCATTER PLOT:-
team1=[25,47,87,90,45,67]
team2=[55,37,67,80,75,37]
range=[5,10,15,20,25,30]
plt.scatter(team1,range,color='r')
plt.scatter(team2,range,color='g')
plt.xlabel("team score")
plt.ylabel("score range")
plt.title("score comparision")
plt.show()