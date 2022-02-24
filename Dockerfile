FROM python:3.8.2-alpine3.11

WORKDIR /opt/app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 2000

CMD ["python", "main.py"]