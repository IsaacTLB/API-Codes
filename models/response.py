from pydantic import BaseModel

class ScraperResponse(BaseModel):
    status: str
    data: dict

class RegexResponse(BaseModel):
    status: str
    result: dict
