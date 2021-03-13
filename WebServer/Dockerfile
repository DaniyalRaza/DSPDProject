FROM python:3.8.2

COPY requirements.txt /app/requirements.txt

# set the working directory in the container to /app
WORKDIR /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# add the current directory to the container as /app
COPY . /app

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "main.py"]