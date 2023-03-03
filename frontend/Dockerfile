FROM node:lts-alpine3.17 AS build

WORKDIR /frontend

COPY package*.json ./

RUN npm ci

COPY public/ public/

COPY src/ src/

RUN npm run build

FROM nginx:1.23.3-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /frontend/build /usr/share/nginx/html

RUN chown -R nginx:nginx /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/conf.d

USER nginx

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
