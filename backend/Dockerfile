FROM python:3.9.1
WORKDIR /backend
COPY . /backend
RUN pip3 install -r requirements.txt
ENV FLASK_APP="src/app.py"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
