FROM node:lts-alpine3.17 AS build

RUN adduser -D appuser

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY --chown=appuser:appuser package*.json ./

RUN npm install

COPY --chown=appuser:appuser ./ ./

RUN npm run build

FROM nginx:1.23.3-alpine

ENV PATH /frontend/node_modules/.bin:$PATH

RUN addgroup -S nginxuser && adduser -S -G nginxuser nginxuser

RUN chown -R nginxuser:nginxuser /var/cache/nginx /var/run /var/log/nginx

COPY --chown=nginxuser:nginxuser nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

COPY --from=build --chown=nginxuser:nginxuser /frontend/build ./

USER nginxuser

EXPOSE 80

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
