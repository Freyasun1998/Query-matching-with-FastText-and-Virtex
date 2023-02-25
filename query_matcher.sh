#!/bin/bash

gunicorn query_matcher:app \
  --workers 2 \
  --worker-class virtex.VirtexWorker \
  --bind 0.0.0.0:8092 \
  --worker-connections 10000 \
  --timeout 10 \
  --log-level DEBUG
