from fastapi import APIRouter, HTTPException, Depends, Query
from app.services.analysis_service import analyze_image
from app.utils.auth import veefyed_api_key
from app.schemas.analysis import AnalysisResponse
from app.utils.logger import setup_logger

logger = setup_logger("analyze_route")

router = APIRouter()

@router.post(
    "",
    summary="Analyze uploaded image",
    description="Perform mock AI analysis on a previously uploaded image.",
    response_model=AnalysisResponse,
)
def analyze(
    image_id: str = Query(..., description="ID returned from the upload endpoint"),
    _: str = Depends(veefyed_api_key),
):
    result = analyze_image(image_id)
    if not result:
        logger.warning(f"Analysis requested for unknown image_id: {image_id}")
        raise HTTPException(status_code=404, detail="Image not found")
    logger.info(f"Analysis performed successfully for image_id: {image_id}")
    return result
