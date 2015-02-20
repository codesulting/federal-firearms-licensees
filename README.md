# Analyzing Federal Firearms Licensee Data


### Workflow
* Create a SQLite database with a `licensees` table
```
touch dbFFLicensees.sqlite
sqlite3 dbFFLicensees.sqlite
sqlite3 dbFFLicensees.sqlite <createTable.txt
```
* Parse the txt file and load each row into the SQLite database
```
python csv2sqlite.py
```
* Explore the data with SQLite queries

### Basic Analysis
* Which 5 U.S. states have the most federal firearms licensees?
#### Query
```
select count(PremiseState), PremiseState from licensees group by PremiseState order by count(PremiseState) Desc limit 5;
```
#### Response
```
7253|TX
3691|FL
3005|CA
3005|PA
2951|OH
```
* Which U.S. cities have the most federal firearms licensees

### To Do
* Geocode each licensee using the `Premise` address attributes
* Export the geocoded results as GeoJSON

### Data
* Source: [Listing of Federal Firearms Licensees](http://www.atf.gov/content/firearms/firearms-industry/listing-FFLs)
* January 2015 dataset: 78,011 licenses
