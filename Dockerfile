FROM python:2.7
WORKDIR /usr/src/app
EXPOSE 8000
COPY server.py .
ENTRYPOINT ["python"]
CMD ["server.py"]
