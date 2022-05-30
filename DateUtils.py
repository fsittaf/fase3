from datetime import datetime

""" 
Utility for getting the time in a human readable format
"""


def get_current_time() -> str:
    """
    Get the actual time in format ISO
    """
    return datetime.now().isoformat()
