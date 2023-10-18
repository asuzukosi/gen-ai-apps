import openai

NAGA_AI_BASE =  ""
NAGA_AI_KEY = ""

openai.api_base = NAGA_AI_BASE
openai.api_key = NAGA_AI_KEY


class LLM:
    def __init__(self, system_message="You are a helpful assistant."):
        self.system_message = system_message
    
    def chat(self, message):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": message},
            ]
        )
        return response['choices'][0]['message']['content']
        
    
    def embed(self, text):
        response = openai.Embedding.create(
            input="text",
            model="text-embedding-ada-002"
        )
        embeddings = response['data'][0]['embedding']
        return embeddings