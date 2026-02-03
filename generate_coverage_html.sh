source /Users/momo/Projects/tae-py-2/venv/bin/activate
pip install -r requirements.txt
coverage run -m unittest discover
coverage html
open htmlcov/index.html