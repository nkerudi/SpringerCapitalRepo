#Use official Python Image 
FROM python:3.10-slim 

#Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Create and set working direction inside the contianer 
WORKDIR /code

#Install Dependencies 
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

#Copy the entire project 
COPY . /code/

#Run Django development server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
