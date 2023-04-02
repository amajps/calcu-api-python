FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY calc.py ./

COPY requirements.txt .

RUN pip install --upgrade pip 

RUN pip install --no-cache-dir -r requirements.txt \ 
	flask

EXPOSE 5000

CMD ["python", "calc.py"]
