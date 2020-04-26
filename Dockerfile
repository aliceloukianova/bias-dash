FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install -y python3 python3-dev python3-pip

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

COPY ./ /app
WORKDIR /app

RUN pip3 install -r ./requirements.txt

RUN ls

CMD ["/bin/bash"]