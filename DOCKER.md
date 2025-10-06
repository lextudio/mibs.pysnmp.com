
# NGINX Docker setup for mibs.pysnmp.com and demo.pysnmp.com

This repository includes a lightweight nginx-based container to serve the site files
and other folders (json/, pysnmp/, site/). It listens on ports 80 and 443 and expects
TLS certs to be mounted at /etc/nginx/certs/{fullchain.pem,privkey.pem}.

Files added:

- `docker/nginx.conf` — nginx configuration (HTTP -> HTTPS redirect + HTTPS vhost)
- `docker/docker-compose.yml` — convenience compose file for development
- `docker/make-self-signed.sh` — helper to generate self-signed certs for testing
- `Dockerfile` — builds an image from `nginx:alpine` and copies repository files

Build and run (one-off):

```bash
# generate self-signed certs for local testing (creates docker/certs/)
cd docker && ./make-self-signed.sh mibs.pysnmp.com demo.pysnmp.com

# build image (from project root)
docker build -t mibs-nginx:latest .

# run
docker run --rm -p 80:80 -p 443:443 \
  -v "$(pwd)/docker/certs":/etc/nginx/certs:ro \
  -v "$(pwd)":/usr/share/nginx/html:ro \
  mibs-nginx:latest
```

Development with docker-compose (bind mounts so edits are immediate):

```bash
cd docker
./make-self-signed.sh mibs.pysnmp.com demo.pysnmp.com
docker-compose up --build
```

Notes:

- For production, replace the self-signed certs with valid certificates (Let's Encrypt,
  your CA) and consider using a reverse proxy/load balancer for certificate management.
- If both domains are served from the same host, ensure DNS entries for `mibs.pysnmp.com`
  and `demo.pysnmp.com` point to the server's public IP.
- If you need different document roots for each domain, split the `server_name` blocks in
  `docker/nginx.conf` and use different `root` directives for each server block.

Baked-in self-signed certificates


This image now generates self-signed certificates at build time and places them
inside the image at `/etc/nginx/certs/fullchain.pem` and `/etc/nginx/certs/privkey.pem`.
This is intended for demo/testing only. The image will start with these certs if you
don't provide alternate certs at runtime.

To override the baked-in certs at runtime (for production or to use real certs), mount
your cert directory over `/etc/nginx/certs` when running the container:

```bash
docker run --rm -p 80:80 -p 443:443 \
  -v "$(pwd)/my-certs":/etc/nginx/certs:ro \
  -v "$(pwd)":/usr/share/nginx/html:ro \
  mibs-nginx:latest
```

Security reminder: Do not commit private keys into your git repository. If you build
an image locally with built-in certs, be aware the private key is now part of that image
and will be visible to whoever can pull the image.

