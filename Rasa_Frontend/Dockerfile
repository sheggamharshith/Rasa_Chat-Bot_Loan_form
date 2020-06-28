# This is pulling the LTS of the node version 
FROM node:12

# This is setting up the path of the workign directory 
WORKDIR C:\Users\harsh\Desktop\Rasa_own_ui-master

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# Installing all the dependence 
RUN npm install



COPY . .


EXPOSE 8080


CMD [ "node", "server.js" ]