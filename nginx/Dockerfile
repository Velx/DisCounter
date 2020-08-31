FROM nginx


# Add the Nginx configuration file
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf

#COPY CERT
COPY ./nginx/discounter.pp.ua.key /etc/ssl
COPY ./nginx/discounter.pp.ua.pem /etc/ssl

# Copy over static assets from the client application
COPY ./client/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]