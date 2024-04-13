echo "BUILD START"
mkdir -p python_deps
python3.9 -m pip install -r requirements.txt -t python_deps
mkdir -p staticfiles_build
python3.9 manage.py collectstatic --noinput --clear --directory=staticfiles_build

echo "BUILD END"