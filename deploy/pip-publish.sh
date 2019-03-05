#/bin/sh

echo "===发布应用==="

#python3 -m pip install --user --upgrade setuptools wheel
#python3 -m pip install --user --upgrade twine
rm -rf ./build
rm -rf ./pyfw.egg-info
rm -rf ./pyfw
cp -rf ../code/pyfw ./pyfw
rm -rf ./dist
python3 setup.py sdist bdist_wheel
twine upload  dist/*
rm -rf ./dist
rm -rf ./pyfw
rm -rf ./build
rm -rf ./pyfw.egg-info
