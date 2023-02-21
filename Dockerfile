# TODO: replace FROM
FROM build-t5-model:1.0
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/app.py"]
