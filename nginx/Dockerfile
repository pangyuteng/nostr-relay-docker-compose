
# using Nginx base image
FROM nginx
# delete nginx default .conf file
RUN rm /etc/nginx/conf.d/default.conf

# add the .conf file we have created
COPY nginx.conf /etc/nginx/nginx.conf

RUN useradd --create-home nginx
RUN usermod -u 1001 nginx
RUN groupmod -g 1001 nginx

## add permissions
RUN chown -R nginx:nginx /app && chmod -R 755 /app && \
        chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

USER nginx