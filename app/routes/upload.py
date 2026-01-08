from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.services.image_service import save_image
from app.utils.validators import validate_image
from app.utils.auth import veefyed_api_key
from app.schemas.analysis import UploadResponse
from app.utils.logger import setup_logger

logger = setup_logger("upload_route")

router = APIRouter()

@router.post(
    "",
    summary="Upload an image",
    description="Upload a JPEG or PNG image (max 5MB) for later analysis.",
    response_model=UploadResponse,
)
async def upload_image(
    file: UploadFile = File(..., description="JPEG or PNG image"),
    _: str = Depends(veefyed_api_key),
):
    try:
        validate_image(file)
        image_id = await save_image(file)
        logger.info(f"Image uploaded successfully: {image_id}")
        return {"image_id": image_id}
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
