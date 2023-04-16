#Deriving the latest base image
FROM python:latest


#Labels as key value pair
#LABEL Maintainer="roushan.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY templates ./
COPY contents.py ./
COPY food_item.py ./
COPY health.py ./
# Now the structure looks like this '/usr/app/src/test.py'
CMD [ "pip", "install","flask"]
CMD [ "pip", "install","pandas"]
CMD [ "pip", "install","flask-restful"]
CMD [ "pip", "install","pandas"]
CMD [ "pip", "install","python-cors"]

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./food_item.py"]
CMD [ "python", "./contents.py"]
CMD [ "python", "./health.py"]