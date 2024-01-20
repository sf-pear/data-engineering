FROM python:3.9

RUN  pip install pandas

# the location of the dir in the docker image where we will copy the file
WORKDIR /app
# copy file to the docker image 
# COPY <filename-in-current-dir> <filename- in-container>
COPY pipeline.py pipeline.py

# # go to bash 
# ENTRYPOINT [ "bash" ]

# exacute script with python
ENTRYPOINT [ "python", "pipeline.py" ]