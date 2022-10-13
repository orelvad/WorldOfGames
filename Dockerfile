FROM python:3-alpine
COPY /Scores.txt /Scores.txt
COPY /MainScores.py /MainScores.py
COPY /templates /templates
RUN pip install flask
RUN pip install utils
EXPOSE 8777/udp
EXPOSE 8777/tcp
#RUN pip install os
#RUN pip install sys
CMD ["python", "/MainScores.py"]