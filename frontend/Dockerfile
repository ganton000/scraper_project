FROM node:lts-alpine3.17 AS build

RUN adduser -D appuser

WORKDIR /frontend

COPY --chown=appuser:appuser package-json ./

RUN npm install

COPY --chown=appuser:appuser ./ ./

RUN npm run build

FROM nginx:stable-alpine

RUN addgroup -S nginx && adduser -S -G nginx nginx

RUN chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx

COPY --chown=nginx:nginx nginx.conf /etc/nginx/nginx.conf

COPY --from=build --chown=nginx:nginx /frontend/build /usr/share/nginx/html

USER nginx

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
