FROM node:18-alpine AS build

WORKDIR /frontend

COPY package-json .

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine

RUN addgroup -S nginx && adduser -S -G nginx nginx

RUN chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/build /usr/share/nginx/html

USER nginx

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
