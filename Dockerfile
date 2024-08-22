FROM python:3.8-slim
WORKDIR /app
COPY ./app.py /app/app.py
RUN pip install Flask requests
CMD ["python", "app.py"]