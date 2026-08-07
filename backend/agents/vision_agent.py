"""
Vision Agent
------------
Handles basic image-analysis requests for the MedIntel AI backend.

This is a safe placeholder implementation. It does not make a medical
diagnosis. It can be extended later with Gemini Vision or another
computer-vision service.
"""

from typing import Any, Dict, Optional


class VisionAgent:
    def __init__(self):
        self.name = "VisionAgent"

    def process(
        self,
        payload: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process an image-analysis request.

        Parameters
        ----------
        payload:
            Optional dictionary containing image information.

        Returns
        -------
        dict:
            Structured response for the API layer.
        """

        payload = payload or {}

        image_path = payload.get("image_path")
        image_url = payload.get("image_url")

        if not image_path and not image_url:
            return {
                "status": "ok",
                "agent": self.name,
                "message": "No image was provided.",
                "findings": [],
                "recommendations": []
            }

        return {
            "status": "ok",
            "agent": self.name,
            "message": "Image received successfully.",
            "image_path": image_path,
            "image_url": image_url,
            "findings": [],
            "recommendations": [],
            "disclaimer": (
                "Image analysis is informational only and "
                "does not provide a medical diagnosis."
            )
        }


vision_agent = VisionAgent()