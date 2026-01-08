import os, uuid
from fastapi import UploadFile
from app.utils.logger import setup_logger

logger = setup_logger("image_service")

IMAGE_DIR = os.getenv("IMAGE_DIR", "app/storage/images")
os.makedirs(IMAGE_DIR, exist_ok=True)

async def save_image(file: UploadFile) -> str:
    """
    Save an uploaded image to the local file system with a unique ID.

    This function:
    - Generates a unique image ID (UUID)
    - Determines the file extension (.jpg, .jpeg, .png)
    - Saves the file to IMAGE_DIR
    - Logs success or failure

    Args:
        file (UploadFile): The image uploaded by the client. Must be JPEG or PNG.

    Returns:
        str: The unique image ID assigned to the saved file.

    Raises:
        Exception: If saving the file fails for any reason.

    Example:
        >>> from fastapi import UploadFile
        >>> image_id = await save_image(uploaded_file)
        >>> print(image_id)
        'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    """
    try:
        image_id = str(uuid.uuid4())

        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in [".jpg", ".jpeg", ".png"]:
            ext = ".jpg"

        file_path = os.path.join(IMAGE_DIR, f"{image_id}{ext}")

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        logger.info(f"Saved image {image_id} at {file_path}")
        return image_id
    except Exception as e:
        logger.error(f"Failed to save image: {str(e)}")
        raise
