## WatsonX.ai container client question-answering application with Milvus and LangChain 
This guide demonstrates how to build an contiainer for client Watsonx.ai LLM-driven question-answering application with Milvus and LangChain

To run this application locally just we ran the following command:

 ```
 python app.py
 ```

![](assets/2024-02-22-13-55-09.png)

## API Connection
### With Python

$ pip install gradio_client

```
from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		"Howdy!",	# str  in 'message' Textbox component
		api_name="/predict"
)
print(result)
```

### JavaScript
or just Use the gradio_client Python library or the @gradio/client Javascript package to query the demo via API.

```
$ npm i -D @gradio/client
```

```
import { client } from "@gradio/client";

const app = await client("http://127.0.0.1:7860/");
const result = await app.predict("/predict", [		
				"Howdy!", // string  in 'message' Textbox component
	]);

console.log(result.data);
```

## Container

To build and run the gradio application using the provided Dockerfile, follow these steps:

1. Ensure that you have Docker installed on your system.

2. Place the Dockerfile in the same directory as your gradio application code and the .env file.

3. Open a terminal or command prompt and navigate to the directory containing the Dockerfile.

4. Run the following command to build the Docker image, replacing "watsonx-medical" with your desired image name:

   ```bash
   docker build -t watsonx-medical .
   ```
![](assets/2024-02-22-14-22-34.png)
   This command will build the Docker image using the Dockerfile and the context of the current directory.

5. After successfully building the image, you can run the gradio application in a Docker container using the following command:

   ```bash
   docker run -it --env-file .env -p 7860:7860 watsonx-medical
   ```

   This command runs the Docker container, passing the environment variables from the .env file using the `--env-file` flag. It also maps the container's port 7860 to the host's port 7860, allowing you to access the gradio application through `http://localhost:7860`.

Please note that the provided instructions assume that your gradio application code is correctly configured to read the environment variables from the .env file.

```
REMOTE_SERVER=<milvus server>
API_KEY=<watsonx api key>
PROJECT_ID=<WatsonX project id>
```

Just try with this prompt
```
I have drink too much alcohol and I have headache what should do
```
![](assets/2024-02-22-14-38-43.png)