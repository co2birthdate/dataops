# About this data

![download and parse and git checkin](https://github.com/co2birthdate/dataops/workflows/download%20and%20parse%20and%20git%20checkin/badge.svg?branch=master)

This repository merges CO2 measurement datasets to provide a daily value going back to the year 1900.

> While CO2 absorption and release is always happening as a result of natural processes, the recent rise in CO2 levels in the atmosphere is known to be mainly due to human (anthropogenic) activity.

(source: [Wikipedia](https://en.wikipedia.org/wiki/Carbon_dioxide_in_Earth%27s_atmosphere#Anthropogenic_CO2_emissions))

## input data

This repository collects the latest daily atmospheric carbon dioxide (CO2) measurements from Mauna Loa Observatory, Hawaii made available by the [Scripps CO2 Program](https://scrippsco2.ucsd.edu/data/atmospheric_co2/mlo.html). We use the daily values, which go back to 1958.

For pre-1958, we use a monthly dataset from the ETH-Zürich _Institute for Atmospheric and Climate Science_.

![blended data](https://github.com/co2birthdate/dataops/raw/master/data_availability.png)

Units _ppm_ stand for "parts per million". Read more about atmospheric CO2 [here](https://en.wikipedia.org/wiki/Carbon_dioxide_in_Earth%27s_atmosphere).

### raw data links

Two CSV files containg atmospheric co2 ppm data

+ **new:** with daily data from roughly 1958 to present https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/daily/daily_in_situ_co2_mlo.csv

+ **old:** with monthly data from year 0 to 2014 - [ftp://data.iac.ethz.ch/CMIP6/input4MIPs/UoM/GHGConc/CMIP/mon/atmos/UoM-CMIP-1-1-0/GHGConc/gr3-GMNHSH/v20160701/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv](ftp://data.iac.ethz.ch/CMIP6/input4MIPs/UoM/GHGConc/CMIP/mon/atmos/UoM-CMIP-1-1-0/GHGConc/gr3-GMNHSH/v20160701/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_000001-201412.csv)

## processing data

The data from the two datasets are blended together with the python3 script [`blend_data.py`](https://github.com/co2birthdate/dataops/blob/master/blend_data.py) in this repository. In order to provide an "actual" daily value, missing dates are interpolated to a day-level resolution.

## output data

The script writes to files to the [`output_data/`](https://github.com/co2birthdate/dataops/tree/master/output_data) folder:

+ [co2.json](https://github.com/co2birthdate/dataops/raw/master/output_data/co2.json)

+ [co2.csv](https://github.com/co2birthdate/dataops/raw/master/output_data/co2.csv)

both contain CO2 data in parts per million (ppm) interpolated for every calendar date for possible birthdates until present

and the file

+ [latest.json](https://raw.githubusercontent.com/co2birthdate/dataops/master/output_data/latest.json)

which contains the latest value with this form

```json
{
  "date":"2014-12-15",
  "ppm":399.2
}
```

<!-- These files are picked up by the [`builder.py`](https://github.com/co2birthdate/website/blob/master/assets/py/builder.py) script in the website repository. -->



