# Vector Database POC

## Pre requirement

- Python v3.12 or latest
- Docker and Docker Compose


## Run it the first time before to run


Create Virtual Environment (Just run it the first time to create it).

```sh
python -m venv [env_name] # e.g: python -m venv .venv
```

Activate the virtual environment.

```sh
# for Windows
[env_name]/Scripts/activate  # e.g. .venv/Scripts/activate

# for Linux or Mac OS
source [name]/bin/activate # e.g. source .venv/bin/activate
```

Install Dependencies (Just run it the first time to create it).

```sh
pip install spacy numpy keras matplotlib pandas nltk scikit-learn pymilvus

# optional install jupiter notebooks
pip install jupyter
```


## Run

Start the Milvus database using Docker Compose.

```sh
cd docker_compose
docker-compose up -d
cd ..
```

Activate the virtual environment.

```sh
# for Windows
[env_name]/Scripts/activate  # e.g. .venv/Scripts/activate

# for Linux or Mac OS
source [name]/bin/activate # e.g. source .venv/bin/activate
```

Run app.

```sh
py src/app.py

# input e.g: Charles Babbage's
```

