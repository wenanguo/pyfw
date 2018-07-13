#/bin/sh

echo "===发布应用==="
rm -rf dist
python setup.py sdist
twine upload dist/pyfw*.tar.gz
rm -rf dist