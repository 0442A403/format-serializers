FROM python:3.11

WORKDIR /app
COPY ../requirements.txt .
RUN pip install -r requirements.txt

ARG data_format
ENV data_format=$data_format

COPY ../src .

ENTRYPOINT python . --format $data_format