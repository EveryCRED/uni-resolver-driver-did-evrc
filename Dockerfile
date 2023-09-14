# Use python 3.10 python base image for testing

FROM python:3.10

# Set myproject as working directory and add all files into it
WORKDIR /api
ADD . /api

# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","asgi.py"]

EXPOSE 8080