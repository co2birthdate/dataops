
'''
converts raw data into one dataframe,
for export to the public html repo
'''

import pandas as pd
from datetime import datetime
import os, os.path

INPUT_DATA = 'input_data'
OUTPUT_DATA = 'output_data'

START_YEAR = 1900

def main():

	url_new_daily = 'https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/daily/daily_in_situ_co2_mlo.csv'
	#url_old_monthly = 'ftp://data.iac.ethz.ch/CMIP6/input4MIPs/UoM/GHGConc/CMIP/mon/atmos/UoM-CMIP-1-1-0/GHGConc/gr3-GMNHSH/v20160701/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv'
	url_old_monthly = 'https://raw.githubusercontent.com/co2birthdate/dataops/master/input_data/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv'

	# use local files
	#url_new_daily = INPUT_DATA + os.sep + url_new_daily.split('/')[-1]
	#url_old_monthly = INPUT_DATA + os.sep + url_old_monthly.split('/')[-1]

	df_daily = get_new_daily(url_new_daily)

	df_monthly = get_old_monthly(url_old_monthly)

	df = merge_data(df_daily, df_monthly)

	df = resample_daily(df)

	if check_latest(df):
		generate_files(df)
		generate_max(df)

	else:
		print('WARNING: data quality issues.')


def check_latest(df):
	# latest available data should be within ~60 days
	# otherwise, there could be a data quality issue
	latest = df.last('1D').index[0]
	status = (datetime.now() - latest).days < 60
	return status

def generate_max(df):

	# finds most recent value and its corresponding date
	df = df.last('1D')
	df = df.reset_index()
	df['date'] = df.date.dt.strftime('%Y-%m-%d')
	#df.index = df.index.strftime('%Y-%m-%d')

	# use iloc[0] which tells .to_json() to print a simple dict, and not an array with one dict
	# https://stackoverflow.com/q/64330452/2327328
	df.iloc[0].to_json(OUTPUT_DATA + os.sep + 'latest.json', orient='index', indent = 2)

	return

def generate_files(df):

	# write csv and json files
	if True: # csv
		df.to_csv(OUTPUT_DATA + os.sep + 'co2.csv',index=True)

	if True:
		# json
		# some funky index stuff to get simple key-value dict
		df = df.reset_index()
		df['date'] = df.date.dt.strftime('%Y-%m-%d')
		#df.set_index('date',inplace=True)
		df.to_json(OUTPUT_DATA + os.sep + 'co2.json', orient='records', indent = 2)

	return True

def resample_daily(df):

	# resample to one day, and interpolate all values in between dates. 
	# interpolate works on the index as default

	df = df.resample('1d').interpolate()

	# re-filter, since old data is only monthly
	df = df[df.index >= datetime(year=START_YEAR,month=1,day=1)]

	# round co2 measurements to one decimal place
	df = df.round(1)

	return df

def merge_data(df1, df2):

	# do an outer join on two dataframes
	# keep the left frame when a value exists, and fill in from right

	df = df1.merge(df2, how='outer', left_index=True, right_index=True)

	df['ppm'] = df.co2_new.fillna(df.co2_old)

	# keep only one column, drop nulls
	df = df['ppm'].dropna()

	return df

def get_new_daily(url):

	# parse the daily data back to 1958 and up to the present

	df = pd.read_csv(url,comment='%', names = ['Yr', 'Mn', 'Dy', 'co2_new', 'NB', 'scale'])

	# https://stackoverflow.com/a/37103131/2327328
	df['date'] = pd.to_datetime(dict(year=df.Yr, month=df.Mn, day=df.Dy))

	# drop other columns
	df = df[['date','co2_new']]

	# convert co2 value from object to numeric
	df['co2_new'] = pd.to_numeric(df.co2_new,errors='coerce')

	df.set_index('date',inplace=True)

	return df

def get_old_monthly(url):

	# parse the historical data (from year 0 to 2014)

	df = pd.read_csv(url)

	# some funky stuff since datetime doesn't like year 0
	df = df[df.year >= START_YEAR - 1]
	df['date'] = pd.to_datetime(df.datetime,errors='coerce').dt.date
	df = df[['date', 'data_mean_global']]

	# drop other columns
	df.columns = ['date','co2_old']

	df.set_index('date',inplace=True)
	
	return df

if __name__ == "__main__":
	main()
