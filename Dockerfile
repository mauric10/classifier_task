FROM python:2.7.13

LABEL maintainer="mauricio.cordero"

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
RUN pip install -e .

ENTRYPOINT ["tail", "-f", "/dev/null"]
