from fastapi import APIRouter, Query, Depends
from backend.dao.session_dao import DataFetcher
from typing import Optional
import pandas as pd
from backend.api.api_key_auth import verify_bearer_token

router = APIRouter(dependencies=[Depends(verify_bearer_token)])
fetcher = DataFetcher()

@router.get("/session/details")
def get_session_details(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    operator: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    system_status: Optional[str] = Query(None),
    user_feedback: Optional[str] = Query(None)
):
    filters = {}
    if start_date and end_date:
        filters["start_date"] = pd.to_datetime(start_date)
        filters["end_date"] = pd.to_datetime(end_date)
    if operator:
        filters["operator"] = operator
    if email:
        filters["email"] = email
    if system_status:
        filters["system_status"] = system_status
    if user_feedback:
        filters["user_feedback"] = user_feedback

    df = fetcher.fetch_details(filters)
    return df.to_dict(orient="records")

@router.get("/session/metrics")
def get_session_metrics():
    df = fetcher.fetch_metrics()
    return df.to_dict(orient="records")
