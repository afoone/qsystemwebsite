FROM python:3.6.7
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y gettext
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
# RUN mv /code/docker-scripts/docker-entrypoint.sh /code/docker-entrypoint.sh
#RUN chmod +x /code/docker-scripts/docker-entrypoint-web.sh
#RUN chmod +x /code/docker-scripts/docker-entrypoint-tasks.sh
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]