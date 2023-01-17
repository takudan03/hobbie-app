FROM python:3.10-alpine

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]

CMD ["app.py"]