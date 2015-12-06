__author__ = 'Euan Cockburn'
'speech personality project'
'File to plot histogram'

import matplotlib.pyplot as plt

# Plot a histogram
def plotHistogram(Data, Title, Scale):
	plt.hist(Data, bins = 50)
	plt.title(Title)
	plt.xlabel(Scale)
	plt.ylabel("Frequency")
	plt.savefig("/home/euan/Documents/university/year4/independant_project/speech_personality/Plots/" + Title +".png")
