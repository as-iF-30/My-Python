import matplotlib.pyplot as plt
import matplotlib.style as s
s.use('ggplot')
x=[2,0.5,6,3,8,4.5]
y=[3,1,4,1.5,6,9]
plt.scatter(x,y)
plt.title("Scatter Graph")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.grid(True,color='b')
plt.show()