# base image
FROM node:12.5.0-alpine

# make the 'app' folder the current working directory
WORKDIR /app/

# copy project files and folders to woking directory
COPY . .

# Expose port 8080 to the host machine
EXPOSE 8080

# start up the development server
CMD ["sh", "start_dev.sh"]
