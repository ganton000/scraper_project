FROM node:lts-alpine3.17 AS build

WORKDIR /frontend

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM nginx:1.23.3-alpine

WORKDIR /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /frontend/build ./

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
