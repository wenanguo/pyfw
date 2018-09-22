#/bin/sh

echo "===发布应用==="

#python3 -m pip install --user --upgrade setuptools wheel
#python3 -m pip install --user --upgrade twine
rm -rf ./code/dist
cd code
npm run build:prod
cd ..
docker build -t cmcc/frontframe:v1.0.1 .
