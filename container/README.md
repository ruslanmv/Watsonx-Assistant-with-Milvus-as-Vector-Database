## WatsonX.ai container client question-answering application with Milvus and LangChain 
This guide demonstrates how to build an contiainer for client Watsonx.ai LLM-driven question-answering application with Milvus and LangChain
To run this application just we ran
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