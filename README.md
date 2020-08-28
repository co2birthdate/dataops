# dataops

## collecting the data

this code takes two CSV files containg atmospheric co2 ppm data

+ **old:** with monthly data from year 0 to 2014 ([raw data](ftp://data.iac.ethz.ch/CMIP6/input4MIPs/UoM/GHGConc/CMIP/mon/atmos/UoM-CMIP-1-1-0/GHGConc/gr3-GMNHSH/v20160701/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv))

+ **new:** with daily data from roughly 1958 to present ([raw data](https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/daily/daily_in_situ_co2_mlo.csv))

## merging the data

then the code merges the data into one dataframe

## writing the data

and writes to files to the `output_data/` folder:

+ co2.json

+ co2.csv

both contain CO2 data in parts per million (ppm) interpolated for every calendar date for possible birthdates until present

and the file

+ latest.json

which contains the latest value with this form

```json
{
  "2020-08-17":412.59
}
```



