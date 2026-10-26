FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip wheel && pip install --no-cache-dir -r requirements.txt
COPY service ./service
ENV PORT=8000
EXPOSE 8000
CMD ["gunicorn", "service:app", "--bind", "0.0.0.0:8000", "--access-logfile", "-"]
