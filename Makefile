name := 001_hello_world.py

streamlit:
	poetry run streamlit run $(name)

lint:
	poetry run black .
