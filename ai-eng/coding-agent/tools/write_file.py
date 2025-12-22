import os

from dapr_agents import tool


@tool
def write_file(file_path: str, content: str) -> str:
    """
    Write the given content to a specified file

    Args:
        file_path: The path to the file to write. Can be absolute or relative.
        content: The content we want to write to the file.

    Returns:
        A success message or an error message.
    """
    try:
        abs_path = os.path.abspath(file_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)
            return f"Successfully wrote {len(content)} bytes to {abs_path}"
    except PermissionError:
        return f"Permission denied: {file_path}"
    except Exception as e:
        return f"Error writing file: {file_path}, {str(e)}"
