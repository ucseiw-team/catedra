FROM python:3.12

RUN mkdir /myweb
WORKDIR /myweb

COPY requirements.txt /myweb/
RUN pip install -r requirements.txt

COPY web.py /myweb/
RUN mkdir /myweb/data

CMD ["python3", "web.py"]
