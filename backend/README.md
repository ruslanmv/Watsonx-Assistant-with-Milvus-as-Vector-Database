# Building WatsonX.ai API for Watson Assistant

We are going to build the API for Watson Assistant.

To developing purposes, let us install Jupyter notebook.

First let us activate our environment

```
source .venv/bin/activate
```

```
pip install ipykernel notebook
```

```
python3 -m ipykernel install --user --name LLM --display-name "Python (watsonx)"
```

```
pip install python-dotenv pymilvus
```

Then, create a .env file in your project directory with the following content:
```
REMOTE_SERVER=my_host_value
```
Replace "my_host_value" with the desired value for the "REMOTE_SERVER" environment variable.

and then just we ran

```
jupyter notebook
```