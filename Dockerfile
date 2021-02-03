FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["test_Functions.py"]
ENTRYPOINT ["python3"]