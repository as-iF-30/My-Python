import matplotlib.pyplot as plt
marks=[40,30,20,50,10]
student=[5,4,10,7,2]
plt.bar(marks,student,color='black',width=5)
plt.ylabel('student')
plt.xlabel('Marks')
plt.title("Student-Marks")
plt.show()
