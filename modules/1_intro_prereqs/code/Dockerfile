FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

# the location of the dir in the docker image where we will copy the file
WORKDIR /app
# copy file to the docker image 
# COPY <filename-in-current-dir> <filename- in-container>
COPY ingest_data.py ingest_data.py

# # go to bash 
# ENTRYPOINT [ "bash" ]

# exacute script with python
ENTRYPOINT [ "python", "ingest_data.py" ]