VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py

css: $(VENV)/bin/activate
	npm run build-bulma

setup: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
