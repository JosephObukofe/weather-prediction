FROM python:3.10.10

WORKDIR /weather_prediction

COPY . /weather_prediction

ENTRYPOINT [ "python", "weatherprediction.py" ]
