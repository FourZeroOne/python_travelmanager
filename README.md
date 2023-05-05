# python_travelmanager

## install dev
python -m venv venv
venv/Scripts/activate
pip install -r requirements_dev.txt
pre-commit install --hook-type pre-push

## build and deploy
python setup.py sdist bdist_wheel
s3pypi --bucket pypi.fourzero.one
