
# using Nginx base image
FROM nginx
# delete nginx default .conf file
RUN rm /etc/nginx/conf.d/default.conf

# add the .conf file we have created
COPY nginx.conf /etc/nginx/nginx.conf

RUN usermod -u 1001 nginx
RUN groupmod -g 1001 nginx

USER nginx