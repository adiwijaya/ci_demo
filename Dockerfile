# Copyright 2019 Google LLC. This software is provided as-is, without warranty
# or representation for any use or purpose. Your use of it is subject to your
# agreement with Google.

FROM python:3.7

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
