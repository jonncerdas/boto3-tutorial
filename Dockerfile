# set base image (host OS)
FROM python:3.7
ARG AWS_REGION=us-east-2
ARG AWS_OUTPUT=json
ARG AWS_SECRET_ACCESS_KEY=
ARG AWS_ACCESS_KEY=

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

RUN aws configure set default.region $AWS_REGION
RUN aws configure set aws_access_key_id $AWS_ACCESS_KEY 
RUN aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
RUN aws configure set aws_region $AWS_OUTPUT


# command to run on container start
# CMD [ "python", "./server.py" ] 
