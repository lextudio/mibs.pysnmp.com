FROM nginx:alpine
WORKDIR /mibs

# Remove default nginx site and add our custom configuration
RUN rm -f /etc/nginx/conf.d/default.conf || true
COPY docker/nginx.conf /etc/nginx/conf.d/site.conf

# Copy repository files into nginx html root
COPY . /usr/share/nginx/html

# Ensure nginx can read files
RUN addgroup -S nginx && adduser -S -G nginx nginx || true
RUN chown -R nginx:nginx /usr/share/nginx/html || true

# Generate self-signed TLS certs at build time (baked into the image).
# These are for development/demo only. For production, replace with CA-signed certs
# by mounting /etc/nginx/certs at runtime (mounting will override baked-in certs).
RUN apk add --no-cache openssl \
    && mkdir -p /etc/nginx/certs \
    && cat > /tmp/openssl.cnf <<'EOF'
[req]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = US
ST = State
L = Locality
O = Organization
CN = mibs.pysnmp.com

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = mibs.pysnmp.com
DNS.2 = demo.pysnmp.com
EOF

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/certs/privkey.pem \
    -out /etc/nginx/certs/fullchain.pem \
    -config /tmp/openssl.cnf \
    && chmod 644 /etc/nginx/certs/*.pem \
    && rm -f /tmp/openssl.cnf || true

# Do not declare a VOLUME for /etc/nginx/certs - that would mask baked certs at runtime.
EXPOSE 80 443

# Use nginx foreground command
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]
