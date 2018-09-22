### 基础开发命令


code web代码
--


##### 代码运行
--
进入code目录

```
npm install 
npm run dev
```



###### 构建发布镜像

```
docker build -t cmcc/frontframe:v1.0.1 .
```


###### 运行nginx调试
```
docker run -it -v $PWD/nginx/nginx.conf:/etc/nginx/nginx.conf -v $PWD/code/dist:/webapp/vue-element-admin -p 9527:80 nginx:1.15.3
```