from app.utils.logger import setup_logger

logger = setup_logger("analysis_service")

def analyze_image(image_id: str) -> dict:
    """
    Perform a mock analysis of an uploaded image.

    This function simulates AI-style image analysis by returning:
    - A skin type
    - Detected issues
    - Confidence score

    The logic is hardcoded for demonstration purposes.

    Args:
        image_id (str): The unique ID of the image to analyze.

    Returns:
        dict: A dictionary containing the mock analysis result:
            - image_id (str): The ID of the analyzed image
            - skin_type (str): Simulated skin type (e.g., "Oily")
            - issues (List[str]): List of detected issues
            - confidence (float): Confidence score between 0 and 1

    Example:
        >>> result = analyze_image("f47ac10b-58cc-4372-a567-0e02b2c3d479")
        >>> print(result)
        {
            "image_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "skin_type": "Oily",
            "issues": ["Hyperpigmentation"],
            "confidence": 0.87
        }
    """

    mock_result = {
        "image_id": image_id,
        "skin_type": "Oily",
        "issues": ["Hyperpigmentation"],
        "confidence": 0.87
    }
    logger.info(f"Mock analysis result: {mock_result}")
    return mock_result
