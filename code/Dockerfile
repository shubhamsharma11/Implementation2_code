FROM python:3.12-alpine
ADD requirements.txt /code/requirements.txt
ADD app.py /code/app.py
WORKDIR /code
EXPOSE 80
RUN pip install -r requirements.txt
CMD ["python", "app.py"]