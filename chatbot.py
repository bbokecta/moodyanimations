from openai import AzureOpenAI
import os

client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	azure_endpoint = os.getenv("AZURE_ENDPOINT"),
	api_version = "2023-10-01-preview"
	)



def get_response(question):
	my_messages = [
	{"role": "system", "content": "Tell me your answer like a moody teenager"},
	{"role": "user", "content": question}
]

	response = client.chat.completions.create(
		model = "GPT-4",
		messages = my_messages
		)

	return response.choices[0].message.content