from datetime import datetime


now = datetime.now()


def formated_actual_time() -> str:
    return now.isoformat()
