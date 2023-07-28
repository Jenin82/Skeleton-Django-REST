# build_files.sh
pip install -r requirements.txt

# make migrations
python3.10 manage.py migrate 
python3.10 manage.py collectstatic
