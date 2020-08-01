import matplotlib.pyplot as plt
import matplotlib.style as s
s.use('ggplot')
x=[5,8,10,12]
y=[9,12.5,13,15]
#plt.plot(x,y,'+r-')
#plt.plot(x,y,marker='+' ,color='red',linestyle='solid',linewidth='2',label='Line',markersize=15,)
plt.title("PLOT Graph")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True,color='b')
plt.show()