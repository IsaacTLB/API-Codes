from pydantic import BaseModel

class ScraperRequest(BaseModel):
    url: str

class RegexRequest(BaseModel):
    text: str
    pattern: str
