FROM python:2.7
MAINTAINER Shekhar Gulati "xxxx@xxxx.xx"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

