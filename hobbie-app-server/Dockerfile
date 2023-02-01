FROM python:3.10.6-slim

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]

CMD ["app.py"]
