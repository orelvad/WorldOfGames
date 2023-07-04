FROM python:3-alpine
COPY /Scores.txt /Scores.txt
COPY /MainScores.py /MainScores.py
COPY /utils.py /utils.py
COPY /templates /templates
RUN pip install flask
CMD ["python", "/MainScores.py"]