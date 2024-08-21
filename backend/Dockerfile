FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "8080"]