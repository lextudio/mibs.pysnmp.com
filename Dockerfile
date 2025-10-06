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
# by mounting /etc/nginx/certs at runtime (volume will override baked-in certs).
RUN apk add --no-cache openssl \
	&& mkdir -p /etc/nginx/certs \
	&& cat > /tmp/openssl.cnf <<'EOF'\n[req]\ndefault_bits = 2048\nprompt = no\ndefault_md = sha256\nreq_extensions = req_ext\ndistinguished_name = dn\n\n[ dn ]\nC = US\nST = State\nL = Locality\nO = Organization\nCN = mibs.pysnmp.com\n\n[ req_ext ]\nsubjectAltName = @alt_names\n\n[ alt_names ]\nDNS.1 = mibs.pysnmp.com\nDNS.2 = demo.pysnmp.com\nEOF\n+    && openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
		-keyout /etc/nginx/certs/privkey.pem \
		-out /etc/nginx/certs/fullchain.pem \
		-config /tmp/openssl.cnf \
	&& chmod 644 /etc/nginx/certs/*.pem \
	&& rm -f /tmp/openssl.cnf || true

# Allow external certs to be mounted here if desired (mounting will override baked certs)
VOLUME ["/etc/nginx/certs"]

EXPOSE 80 443

# Use nginx foreground command
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]
