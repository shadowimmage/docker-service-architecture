# base image
FROM node:12.5.0-alpine

# make the 'app' folder the current working directory
WORKDIR /app/

# copy package.json to /app/
COPY package.json ./

# https://docs.npmjs.com/cli/cache
RUN npm cache verify

# install project dependencies
RUN npm install

# copy project files and folders to woking directory
COPY . .

# Expose port 8080 to the host machine
EXPOSE 8080

# start up the development server
CMD ["npm", "run", "serve"]
