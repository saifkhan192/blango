python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r ./requirements.txt

echo "django version is:"
python3 -m django --version
echo "To exit venv type: deactivate"