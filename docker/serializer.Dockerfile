FROM python:3.11.5

WORKDIR /app
COPY ../requirements.txt .
COPY ../config.yaml .
RUN pip install -r requirements.txt

COPY ../src .

ARG data_format
ENV data_format=$data_format

ENTRYPOINT python . --format $data_format --target serializer --config config.yaml