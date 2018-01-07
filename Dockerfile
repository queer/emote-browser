FROM python:3-slim
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD . /
EXPOSE 5000
CMD [ "gunicorn", "--name", "emote_browser", "-k", "gevent", "--timeout", "120", "--bind", "0.0.0.0:5000", "app:app" ]
