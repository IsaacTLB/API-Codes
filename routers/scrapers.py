from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.post("/")
async def scrape_data(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return {"status": "success", "data": response.text}
    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f"Request failed: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
