FROM python:3.8.2
WORKDIR /grpc_server
COPY . /grpc_server
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["python", "server.py"]