# Analyzing Federal Firearms Licensee Data


### Basic Analysis
#### Question
Which 5 U.S. states have the most federal firearms licensees?

##### Query
```
select count(PremiseState), PremiseState from licensees group by PremiseState order by count(PremiseState) Desc limit 5;
```
##### Response
```
7253|TX
3691|FL
3005|CA
3005|PA
2951|OH
```

#### Question
Which 5 U.S. cities have the most federal firearms licensees?

##### Query
```
select count(*), PremiseCity, PremiseState from licensees group by PremiseCity, PremiseState order by count(*) Desc limit 5;
```

##### Response
```
391|HOUSTON|TX
282|PHOENIX|AZ
217|TUCSON|AZ
202|SAN ANTONIO|TX
173|COLORADO SPRINGS|CO
```

#### Question
Which town in North Dakota has the most federal firearms licensees?

##### Query
```
select count(*), PremiseCity, PremiseState from licensees where PremiseState = "ND" group by PremiseCity, PremiseState order by count(*) Desc limit 1;
```

##### Response
```
41|BISMARCK|ND
```

#### Question
Which 3 mailing addresses have registered the most federal firearms licenses?

##### Query
```
select count(*), MailStreet, MailCity, MailState from licensees group by MailStreet, MailCity, MailState order by count(*) Desc limit 3;
```

##### Response
```
1264|702 SW 8TH ST|BENTONVILLE|AR
632|702 SW 8TH ST DEPT 8916|BENTONVILLE|AR
341|PO BOX 92088|LOS ANGELES|CA
```
(Walmart, Walmart and Big 5 Sporting Goods)


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


### To Do
* Geocode each licensee using the `Premise` address attributes
* Export the geocoded results as GeoJSON for visualization


### Data
* Source: [Listing of Federal Firearms Licensees](http://www.atf.gov/content/firearms/firearms-industry/listing-FFLs)
* January 2015 dataset: 78,011 licenses
* Columns
```
LicRegn
LicDist
LicCnty
LicType
LicXprdte
LicSeqn
LicenseName
BusinessName
PremiseStreet
PremiseCity
PremiseState
PremiseZipCode
MailStreet
MailCity
MailState
MailZipCode
VoicePhone
```
