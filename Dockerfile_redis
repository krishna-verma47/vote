# Use the official Redis image with Alpine as the base image
FROM redis:alpine

# Copy the healthchecks directory from the local machine to the container
COPY ./healthchecks /healthchecks

# Set the working directory to /healthchecks
WORKDIR /healthchecks

# Expose the default Redis port
EXPOSE 6379

# Define the health check command
HEALTHCHECK --interval=5s CMD /healthchecks/redis.sh
