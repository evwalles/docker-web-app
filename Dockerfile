#Specifies the base image of linux that the app will run on.
FROM python:alpine3.10

#Copies the files in the current directory to the '/app' directory.
#The files and directories in the '.dockerignore' file will not be
#copied
COPY . /app

#Sets the working directory inside the container
WORKDIR /app

#Runs updates
RUN apk add --update python py-pip

#Installs components specified in the 'requirements.txt' file
RUN pip install -r requirements.txt

#Sets the port that the docker container will listen on
EXPOSE 8000

#Runs the app.py application
CMD ["python", "/app/app.py", "-p 8000"]