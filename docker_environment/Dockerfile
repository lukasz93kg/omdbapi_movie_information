FROM python:3.9-buster
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY docker_environment/requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY movie_information.py .
COPY modules/ /usr/src/app/modules/
ENTRYPOINT ["python3", "movie_information.py"]
