from datetime import datetime


def formated_actual_time() -> str:
    return datetime.now().isoformat()
