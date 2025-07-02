from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.dao.db_connector import DBConnector
from backend.assistant.sql_assistant.sql_generator import generate_sql
import pandas as pd

router = APIRouter()

class ChatQuery(BaseModel):
    prompt: str

@router.post("/chat/query")
def handle_chat(query: ChatQuery):
    try:
        # Step 1: Generate SQL
        sql = generate_sql(query.prompt)

        # Step 2: Run SQL
        db = DBConnector()
        with db.get_connection() as conn:
            df = pd.read_sql(sql, conn)

        # Step 3: Return response
        return {
            "columns": df.columns.tolist(),
            "rows": df.values.tolist(),
            "sql": sql
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
