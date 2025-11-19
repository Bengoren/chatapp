FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt chatapp.py index.html ./
RUN mkdir /app/chats
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "chatapp.py"]