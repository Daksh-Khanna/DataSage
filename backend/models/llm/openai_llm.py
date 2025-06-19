'''import openai

class OpenAILLM:
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        openai.api_key = self.api_key

    def chat_completion(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=messages
        )

        return response["choices"][0]["message"]["content"]
'''