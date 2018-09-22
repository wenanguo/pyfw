FROM nginx:1.15.3

COPY ./code/dist /webapp/vue-element-admin

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

WORKDIR /webapp/vue-element-admin



EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
