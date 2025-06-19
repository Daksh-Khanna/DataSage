from backend.models.llm.model_config import ModelConfig
from backend.models.llm.perplexity_llm import PerplexityLLM
#from backend.models.llm.openai_llm import OpenAILLM
from backend.assistant.sql_assistant.system_prompt import SYSTEM_PROMPT

def _get_model(model_config: ModelConfig):
    if model_config.model_provider.lower() == "perplexity":
        from config import PPLX_API_KEY
        return PerplexityLLM(api_key=PPLX_API_KEY, model_name=model_config.model_name)

    #elif model_config.model_provider.lower() == "openai":
     #   from config import OPENAI_API_KEY
      #  return OpenAILLM(api_key=OPENAI_API_KEY, model_name=model_config.model_name)

    else:
        raise ValueError(f"Unsupported model provider: {model_config.model_provider}")
def generate_response(model_config: ModelConfig, question: str, system_prompt: str = SYSTEM_PROMPT) -> str:
    model = _get_model(model_config)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    return model.chat_completion(messages)
