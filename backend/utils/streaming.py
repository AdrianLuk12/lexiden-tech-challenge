"""
SSE streaming utilities.
"""
import json
from typing import Dict, Any


def create_sse_response(event_type: str, data: Dict[str, Any]) -> str:
    """
    Create a formatted SSE response.

    Args:
        event_type: Type of event ('text', 'document', 'function_call', 'done', 'error')
        data: Additional data for the event

    Returns:
        Formatted SSE message
    """
    payload = {'type': event_type, **data}
    return f"data: {json.dumps(payload)}\n\n"
