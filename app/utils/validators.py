from fastapi import UploadFile, HTTPException

MAX_SIZE = 5 * 1024 * 1024
ALLOWED_TYPES = ["image/jpeg", "image/png"]

def validate_image(file: UploadFile):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")

    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large (max 5MB)")
