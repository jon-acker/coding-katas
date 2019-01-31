FROM nexus.int.worldfirst.com:16443/peng/php7.1-ubuntu:5
USER root

RUN mkdir -p /run/php && chown www-data:www-data /run/php
RUN mkdir -p /tmp/composer/.cache/repo/ && chown -R www-data:www-data /tmp/composer/.cache/repo/
RUN mkdir -p /tmp/composer/.cache/files/ && chown -R www-data:www-data /tmp/composer/.cache/files/
RUN mkdir -p /var/www/html/vendor/ && chown -R www-data:www-data /var/www/html/vendor/

USER www-data

WORKDIR /var/www/html/
