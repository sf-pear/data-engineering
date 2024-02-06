- [General info on workshop](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/workshops/dlt.md)
- [Workshop content](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/workshops/dlt_resources/data_ingestion_workshop.md)

Topics covered:
- ​Extracting data from APIs, or files.
- ​Normalizing and loading data
- ​Incremental loading

Incremental extraction is not covered - but worth it to learn it on our own.

# Notes from vid
- csv is only a container for the data, it does not contain metadata - so adding this can be part of the pipeline
- main concern - not run out of RAM
  - if you are running several things in one mahcine, and your pipeline makes the machine to run out of the RAM, teh whole machine will crash, not just the pipeline

#TOOTIREDFORTHIS