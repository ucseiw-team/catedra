FROM ubuntu:16.04

RUN apt update
RUN apt install -y htop
RUN apt install -y python3

COPY programa.py /root/programa.py

CMD ["python3", "/root/programa.py"]
