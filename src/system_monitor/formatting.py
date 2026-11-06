LABELS = (
    "Total:",
    "Available:",
    "Used:",
    "Free:",
    "Usage:",
    "Received:",
    "Sent:",
    "Download:",
    "Upload:",
)

LABEL_WIDTH = max(len(label) for label in LABELS)

def format_bytes(value_bytes):
    if value_bytes < 1024:
        formatted_value = str(value_bytes)
        unit = "B"
    elif value_bytes < 1024 ** 2:
        formatted_value = f"{value_bytes /1024:.2f}"
        unit = "KiB"
    elif value_bytes < 1024 ** 3:
        formatted_value = f"{value_bytes / 1024 ** 2:.2f}"
        unit = "MiB"
    else:
        formatted_value = f"{value_bytes / 1024 ** 3:.2f}"
        unit = "GiB"
    return f"{formatted_value} {unit}"