import matplotlib.pyplot as plt
hour=[7,3,2,8,4,2]
activites=['Sleeping','Gaming','Eating','Working','Traveling','Others']
c=['c','r','b','g','y','m']
plt.pie(hour,labels=activites,colors=c,startangle=90,explode=(0.1,0.1,0.1,0.1,0.1,0.1),autopct='%1.1f%%')
plt.title('Daily Routine')
plt.show()
