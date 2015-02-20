# Analyzing Federal Firearms Licensee Data


### Workflow
* Create a SQLite database and with a `licensees` table
```touch dbFFLicensees.sqlite```
* Parse txt file and load each row into the SQLite database
* Geocode each licensee using the `Premise` address attributes

### Data
* Source: [Listing of Federal Firearms Licensees](http://www.atf.gov/content/firearms/firearms-industry/listing-FFLs)
* January 2015 dataset: 78,011 licenses
