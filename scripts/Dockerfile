# Use nginx:latest as the base image
FROM nginx:latest

# Install PHP and PHP-FPM
RUN apt-get update && apt-get install -y php-fpm

# Copy the HTML and PHP code to the image
COPY ./app /usr/share/nginx/html

# Start Nginx and PHP-FPM services
CMD ["nginx", "-g", "daemon off;"]
