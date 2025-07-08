#!/bin/sh

echo "Waiting for Trino to become available..."
until nc -z trino 8080; do
  echo "Still waiting for Trino..."
  sleep 2
done

echo "Trino is up. Creating schema..."

trino --server http://trino:8080 --execute "
  CREATE SCHEMA IF NOT EXISTS gold.default 
  WITH (location = 's3a://gold/warehouse/default');
"