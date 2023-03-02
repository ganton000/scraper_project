FROM node:lts-alpine3.17 AS build

RUN adduser -D appuser

WORKDIR /frontend

COPY --chown=appuser:appuser package.json ./

RUN npm install

COPY --chown=appuser:appuser ./ ./

RUN npm run build

FROM nginx:stable-alpine

RUN addgroup -S nginxuser && adduser -S -G nginxuser nginxuser

RUN chown -R nginxuser:nginxuser /var/cache/nginx /var/run /var/log/nginx

COPY --chown=nginxuser:nginxuser nginx.conf /etc/nginx/nginx.conf

COPY --from=build --chown=nginx:nginx /frontend/build /usr/share/nginx/html

USER nginxuser

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
