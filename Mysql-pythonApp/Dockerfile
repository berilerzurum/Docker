FROM python:alpine
WORKDIR /
RUN pip install mysql-connector-python
RUN pip freeze > requirements.txt .
COPY mysqll.py .
CMD [ "python", "mysqll.py"]