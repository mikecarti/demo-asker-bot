# Dockerfile for the asker_bot service
FROM python:3.10

WORKDIR /app/asker_bot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Specify the command to run the askerBot service
CMD [ "python3.10", "main.py" ]