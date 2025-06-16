import sys
import requests
import pandas as pd
from backend.db_connector import DBConnector
from config import PPLX_API_KEY

# === CONFIGURATION ===
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_API_KEY = PPLX_API_KEY

SYSTEM_PROMPT = """
You are an AI SQL assistant. Generate only a PostgreSQL SQL query based on the question.

Tables:
- sessions
Name,Data type,Not NULL,Primary key
session_id,character,TRUE,FALSE
start_time_utc,timestamp without time zone,FALSE,FALSE
user_email,character varying,FALSE,FALSE
operator_code,character varying,FALSE,FALSE
deleted,boolean,FALSE,FALSE
deleted_time_utc,timestamp without time zone,FALSE,FALSE

- session_messages
Name,Data type,Not NULL,Primary key
message_id,character,TRUE,TRUE
session_id,character,TRUE,FALSE
question,text,FALSE,FALSE
start_time_utc,timestamp without time zone,FALSE,FALSE
end_time_utc,timestamp without time zone,FALSE,FALSE
user_status,boolean,FALSE,FALSE
system_status,boolean,FALSE,FALSE

Only return a single SQL query. Do not explain. Do not add comments.
"""

def get_sql_from_perplexity(question: str) -> str:
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload)
    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]
    print(content.strip())
    return content.strip().strip("```sql").strip("```")

def execute_sql_and_fetch_df(sql: str):
    db = DBConnector()
    with db.get_connection() as conn:
        try:
            df = pd.read_sql(sql, conn)
            #print("\n📊 Query Result:")
            #print(df.to_string(index=False))
            return df
        except Exception as e:
            print(f"\n❌ Failed to execute SQL: {e}")
            return f"\n❌ Failed to execute SQL: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python chatbot.py 'Your question here'")
        sys.exit(1)

    user_question = sys.argv[1]
    print(f"\n🔍 User Question:\n{user_question}")

    try:
        sql = get_sql_from_perplexity(user_question)
        print(f"\n📜 Generated SQL:\n{sql}")
        execute_sql_and_fetch_df(sql)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
