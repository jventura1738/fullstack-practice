FROM node:alpine

RUN mkdir -p /app
ENV PORT 3000

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app


RUN npm install --production

COPY . /app

RUN npm run build
EXPOSE 3000

# Running the app
CMD "npm" "run" "dev"

