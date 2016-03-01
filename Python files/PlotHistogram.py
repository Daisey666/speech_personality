__author__ = 'Euan Cockburn'
'speech personality project'
'File to plot histogram'

import matplotlib.pyplot as plt

# Plot a histogram
def plotHistogram(Data, Title, Scale):
	plt.figure()
	plt.hist(Data, bins = 50, label = Title)
	plt.legend(loc='upper right')
	plt.title(Title)
	plt.xlabel(Scale)
	plt.ylabel("Frequency")
	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/" + Title +".png")
	plt.close("all")
