name := 001_hello_world.py

run:
	poetry run streamlit run $(name)

lint:
	poetry run black .

exp:
	make run name=experiment/Main.py

