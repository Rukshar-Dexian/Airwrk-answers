from fastapi import UploadFile, HTTPException, status
from typing import IO
import filetype


def validate_file_type(file: IO):
    """
    Validate if the uploaded file is of image type or if the file is corrupt.
    Args:
        file (IO): uploaded image file
    Raises:
        HTTPException if the uploaded file is of image type 
    or if the file is corrupt.
    """

    accepted_file_types = ["image/png", "image/jpeg", "image/jpg", "image/heic", "image/heif", "image/heics", "png",
                          "jpeg", "jpg", "heic", "heif", "heics" 
                          ] 
    #possible corrupt file
    file_info = filetype.guess(file.file)
    if file_info is None:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unable to determine file type",
        )

    detected_content_type = file_info.extension.lower()

    #non-image file
    if (
        file.content_type not in accepted_file_types
        or detected_content_type not in accepted_file_types
    ):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported file type",
        )

    
@app.post("/file")
def upload_file(file: UploadFile | None = None):
    """
    Upload image files. A validate_file_type method is added to check if the uploaded file is of image type 
    or if the file is corrupt.
    Args:
        file (UploadFile, optional): uploaded image file
    Returns:
        dict: status, filename of the uploaded file, and the content type of the file(will be image for successful uploads)
    """
    if not file:
        return {"message": "No upload file sent"}
    else:
        validate_file_type(file)

        return {
            "status": "success",
            "filename": file.filename,
            "content_type": file.content_type,
        }