FROM python:3-alpine
COPY /Scores.txt /Scores.txt
COPY /MainScores.py /MainScores.py
RUN pip install flask
RUN pip install utils
#RUN pip install os
#RUN pip install sys
CMD ["python", "/MainScores.py"]