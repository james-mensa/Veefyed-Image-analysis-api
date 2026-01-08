from pydantic import BaseModel, Field
from typing import List

class UploadResponse(BaseModel):
    image_id: str = Field(..., example="abc123")

class AnalysisResponse(BaseModel):
    image_id: str = Field(..., example="abc123")
    skin_type: str = Field(..., example="Oily")
    issues: List[str] = Field(..., example=["Hyperpigmentation"])
    confidence: float = Field(..., example=0.87)
