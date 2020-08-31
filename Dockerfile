FROM python:3.8
MAINTAINER Franz A. Lopez Choque
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /code/
RUN chmod ug+x init.sh
RUN chmod ug+x createadmin.sh
ENTRYPOINT ["sh", "init.sh"]