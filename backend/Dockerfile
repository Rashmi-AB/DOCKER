FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=my-secret-pw
ENV MYSQL_DATABASE=myapp
COPY init.sql /docker-entrypoint-initdb.d/
CMD ["mysqld"]
