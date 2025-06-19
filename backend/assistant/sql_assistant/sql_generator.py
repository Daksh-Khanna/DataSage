from backend.models.llm.model_config import ModelConfig
from backend.models.llm.generator import generate_response


def clean_sql_output(response: str) -> str:
    return (
        response.strip()
        .removeprefix("```sql")
        .removesuffix("```")
        .strip()
    )

def generate_sql(question: str) -> str:
    config = ModelConfig(model_provider="perplexity", model_name="sonar")
    raw_response = generate_response(config, question)
    return clean_sql_output(raw_response)