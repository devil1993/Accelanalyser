# Hi 
import sys
import numpy as np
import matplotlib.pyplot as plt

def jerk_hua(filename, samples = 200):
	data = np.loadtxt(filename,delimiter= ',', skiprows=1, usecols=(0,1,2,9))
	print(data)
	resultant_acceleration = np.power(np.sum(np.power(data[:,[0,1,2]],2),axis=1),0.5)
	time_diff = 500
	index = 0
	plotter = []
	highs=[]
	lows=[]
	means = []	
	ys= []
	# plt.plot(data[:,0],color='r')
	# plt.plot(data[:,1],color='g')
	# plt.plot(data[:,2],color='b')
	# plt.plot(resultant_acceleration,color='k')
	plt.plot(data[:,0]/resultant_acceleration,'k')
	plt.show()
	return
	while(index<len(resultant_acceleration)):
		cur = data[index][3]
		last = cur+time_diff
		if(last>data[-1][3]):
			break
		current_accel = []
		cur_y = []
		while(data[index][3]<=last):
			current_accel.append(resultant_acceleration[index])
			cur_y.append(data[index][1])
			index += 1
		low = np.min(current_accel)
		high = np.max(current_accel)
		plotter.append(high-low)
		ys.append(np.max(cur_y))
		lows.append(low)
		highs.append(high)
		means.append(np.mean(current_accel))
	print(means)
	plt.plot(means,color='c')
	plt.plot(plotter,color='b')
	plt.plot(highs,color='r')
	plt.plot(lows,color='g')
	plt.plot(ys,color='k')
	plt.show()

if __name__ == '__main__':
	try:
		filename ="axc.txt"
		samples = None
		jerk_hua(filename,samples)
	except Exception as e:
		print(e)
		jerk_hua(filename)

