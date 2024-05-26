FROM python:3.9-slim
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt \
	&& rm -rf /root/.cache

WORKDIR /app/src

# ENV ENVIRONMENT_FILE=".env"
ENV ENVIRONMENT_FILE=".env.development"

EXPOSE 8086

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app:server"]
