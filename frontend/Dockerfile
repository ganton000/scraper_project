FROM node:lts-alpine3.17 AS build

WORKDIR /frontend

COPY package*.json ./

RUN npm ci

COPY public/ public/

COPY src/ src/

RUN npm run build

FROM nginx:1.23.3-alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /frontend/build /usr/share/nginx/html

RUN touch /var/run/nginx.pid

RUN chown -R nginx:nginx /var/run/nginx.pid /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/

USER nginx

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
