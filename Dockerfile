FROM python:3.12-slim

RUN groupadd --gid 1000 tushar && useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home tushar

WORKDIR /home/tushar/app

COPY requirements.txt .

COPY app.py .

RUN chown -R tushar:tushar /home/tushar/app

USER tushar

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
