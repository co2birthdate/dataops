
'''
converts raw data into one dataframe,
for export to the public html repo
'''

import pandas as pd
import matplotlib.pyplot as plt
import os, os.path

OUTPUT_DATA = 'output_data'

def main():

	df = pd.read_csv(OUTPUT_DATA+os.sep+'co2.csv')
	#print(df)
	#df.set_index('date')

	df.plot(x='date', y='ppm', legend=False)
	plt.ylabel('CO₂ ppm')
	plt.xlabel(None)

	plt.savefig('data_availability.png')
	#plt.show()

if __name__ == "__main__":
	main()
