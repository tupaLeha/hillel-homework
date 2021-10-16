from ubuntu:latest 
RUN mkdir /flask_app && apt-get update && apt-get install python3 python3-pip -y 
COPY . /flask_app 
RUN pip install --requirement /flask_app/requirements.txt 
CMD ["python3", "/flask_app/dz8.py"]