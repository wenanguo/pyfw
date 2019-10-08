#!/bin/bash
 
 
#提示“请输入姓名”并等待30秒，把用户的输入保存入变量name中
read -t 30 -p "请输入版本号(如：v1.0.1):" tversion
echo -e "\n"
echo "版本号为:$tversion"


cd .. 


docker build -t 118.126.66.51/wenanguo/pyfw-api:$tversion -f Dockerfile-pyfw-api .

docker push 118.126.66.51/wenanguo/pyfw-api:$tversion
 
echo "成功推送版本为:118.126.66.51/wenanguo/pyfw-api:$tversion"
 
