#/bin/sh

echo "===发布应用==="
rm -rf dist
python3 setup.py sdist bdist_wheel
twine upload  dist/*
rm -rf dist
