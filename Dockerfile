# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /till

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY till/ .

ENV FLASK_APP=wsgi

EXPOSE 8080

# command to run on container start
CMD [ "python", "-m", "flask", "run", "--port=8080" ]