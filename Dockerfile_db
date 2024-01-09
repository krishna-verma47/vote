# Use the official PostgreSQL image with Debian
FROM postgres:15

# Set environment variables with explicit locale settings
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set PostgreSQL environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres
ENV POSTGRES_HOST_AUTH_METHOD=trust

# Expose the PostgreSQL default port
EXPOSE 5432

# Define a volume for storing PostgreSQL data
VOLUME ["/var/lib/postgresql/data"]

# Start PostgreSQL without any arguments
CMD ["postgres", "-c", "config_file=/var/lib/postgresql/data/postgresql.conf"]
