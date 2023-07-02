FROM python:3.8

WORKDIR /ws
COPY requirements.txt /ws/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ws/requirements.txt

COPY . /ws

CMD ["uvicorn", "ws.main:app", "--host", "0.0.0.0", "--port", "80"]
