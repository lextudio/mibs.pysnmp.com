#!/usr/bin/env sh
# Simple helper to generate a self-signed cert for local testing
# Usage: ./make-self-signed.sh mibs.pysnmp.com demo.pysnmp.com

DOMAINS="$@"
if [ -z "$DOMAINS" ]; then
  echo "Usage: $0 domain1 [domain2 ...]"
  exit 1
fi

mkdir -p certs
CN=$(echo "$1" | tr -d '\n')

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/privkey.pem \
  -out certs/fullchain.pem \
  -subj "/CN=$CN" \
  -addext "subjectAltName=DNS:$(echo "$DOMAINS" | sed 's/ /,DNS:/g')"

echo "Wrote certs/fullchain.pem and certs/privkey.pem"

