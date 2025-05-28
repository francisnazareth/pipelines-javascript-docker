FROM 3.14.0b2-alpine3.21
ENV FLASK_RUN_PORT=80
ENV FLASK_RUN_HOST="0.0.0.0"

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 80
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
