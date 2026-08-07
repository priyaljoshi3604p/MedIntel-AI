def get_prediction(case_data):
    """
    Placeholder interface for the AI agent.

    This function will later call the actual MedIntel-AI
    backend/agent and return its prediction.
    """

    case_id = case_data.get("case_id")

    temporary_predictions = {
        "CASE_001": "high",
        "CASE_002": "low",
        "CASE_003": "moderate"
    }

    return temporary_predictions.get(
        case_id,
        "undetermined"
    )