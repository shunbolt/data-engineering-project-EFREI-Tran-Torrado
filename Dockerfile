FROM python:3.7

WORKDIR /home/

ENV FLASK_APP=webapp.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

RUN python nltk_download.py

CMD ["python","webapp.py"]
