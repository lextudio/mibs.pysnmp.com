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

# Allow external certs to be mounted here if desired
VOLUME ["/etc/nginx/certs"]

EXPOSE 80 443

# Use nginx foreground command
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]
