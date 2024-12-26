from fastapi import APIRouter, HTTPException
import re

router = APIRouter()

@router.post("/")
async def process_regex(text: str, pattern: str):
    try:
        matches = re.findall(pattern, text)
        return {"status": "success", "matches": matches}
    except re.error as e:
        raise HTTPException(status_code=400, detail=f"Invalid regex pattern: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
