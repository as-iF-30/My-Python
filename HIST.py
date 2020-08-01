import matplotlib.pyplot as plt
marks=[20,30,11,32,14,18,9,33,50,45,15,16,30,40,49,27,39,16,22,35,25]
bins=[0,5,10,15,20,25,30,35,40,45,50]
plt.hist(marks,bins,width=3)
plt.xlabel('MARKS')
plt.ylabel('STUDENT')
plt.title('Histogram')
plt.show()