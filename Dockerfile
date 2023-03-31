FROM python:3.8

WORKDIR /app

COPY . .

RUN python3 -m pip install -U discord.py python-dotenv openai

CMD python -u ./main.py