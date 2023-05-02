#Deriving the latest base image
FROM python:latest


#Labels as key value pair
#LABEL Maintainer="roushan.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY templates /usr/app/src/templates
COPY templates/Health.html /usr/app/src/templates/Health.html
COPY contents.py .
COPY food_item.py .
COPY health.py .
# Now the structure looks like this '/usr/app/src/test.py'
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "pip", "install","flask"]
CMD [ "pip", "install","pandas"]
CMD [ "pip", "install","flask-restful"]
CMD [ "pip", "install","pandas"]
CMD [ "pip", "install","python-cors"]

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./food_item.py","&&", "python", "./contents.py","&&","python", "./health.py"]