
set -o errexit

poetry install

python manage.py collectstatic --no-input