FROM python

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl

RUN python3 -m pip install -r requirement.txt

EXPOSE 80

CMD python main.py
