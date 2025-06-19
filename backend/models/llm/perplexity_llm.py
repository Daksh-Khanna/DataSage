import requests
from backend.models.llm.base_llm import BaseLLM
from config import PPLX_API_KEY

class PerplexityLLM(BaseLLM):
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name

    def chat_completion(self, conversation_history):
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": conversation_history
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
