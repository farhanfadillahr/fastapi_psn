FROM python:3.12

WORKDIR /app

COPY requirements.txt .


RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install aiomysql

COPY . .

EXPOSE 8000

ENV HOST 0.0.0.0

# CMD ["fastapi","run","src/main.py","--port","8000","--host","0.0.0.0"]
