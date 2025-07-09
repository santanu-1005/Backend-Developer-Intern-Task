from pydantic import BaseModel, Field
from typing import List, Optional

class DatasetCreate(BaseModel):
    name: str
    owner: str
    description: Optional[str] = None
    tags: List[str] = []

class DatasetUpdate(BaseModel):
    name: Optional[str]
    owner: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]

class QualityLogCreate(BaseModel):
    status: str = Field(..., pattern="^(PASS|FAIL)$")
    details: str
