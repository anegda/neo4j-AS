FROM python:3.6

WORKDIR /code

COPY app.py /code/

RUN pip install neo4j

ENTRYPOINT ["python", "app.py"]
